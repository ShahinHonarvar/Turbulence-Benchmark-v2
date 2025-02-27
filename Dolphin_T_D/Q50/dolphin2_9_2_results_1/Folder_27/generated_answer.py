def if_contains_anagrams(lst):
    count = 0
    anagrams = {}
    for s in lst:
        if len(s) >= 3:
            ssorted = ''.join(sorted(s.lower()))
            anagrams[ssorted] = anagrams.get(ssorted, 0) + 1
    for k in anagrams:
        if anagrams[k] > 1:
            count += anagrams[k] * (anagrams[k] - 1) // 2
    return count >= 86