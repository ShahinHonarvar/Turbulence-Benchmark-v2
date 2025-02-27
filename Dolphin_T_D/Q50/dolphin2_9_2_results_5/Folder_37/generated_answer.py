def if_contains_anagrams(lst):
    anagrams = {}
    for word in lst:
        if len(word) >= 3:
            key = ''.join(sorted(word.lower()))
            if key not in anagrams:
                anagrams[key] = [word]
            else:
                anagrams[key].append(word)
    pairs = 0
    for key in anagrams:
        if len(anagrams[key]) >= 2:
            pairs += len(anagrams[key]) - 1
            if pairs >= 29:
                return True
    return False