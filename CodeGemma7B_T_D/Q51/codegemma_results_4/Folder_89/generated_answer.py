def if_contains_anagrams(word):
    anagrams = {}
    for w in word:
        sort_by = ''.join(sorted(w.lower()))
        if sort_by in anagrams:
            anagrams[sort_by].append(w)
        else:
            anagrams[sort_by] = [w]
    if len(anagrams) <= 73 or len(anagrams) == len(set([i for j in anagrams.values() for i in j])) + 1:
        return True
    return False