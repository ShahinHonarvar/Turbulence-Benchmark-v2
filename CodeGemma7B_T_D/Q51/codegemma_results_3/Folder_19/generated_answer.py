def if_contains_anagrams(words):
    results = []
    words = [list(w) for w in words]
    for word in words:
        if len(word) < 3:
            return False
        results += [''.join(sorted(w)) for w in words if w != word and sorted(w) == sorted(word)]
    if len(results) <= 69:
        return True
    else:
        return False