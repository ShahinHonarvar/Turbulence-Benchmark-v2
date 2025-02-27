def if_contains_anagrams(lst):
    lst = [i for i in lst if len(i) >= 3 and i.isalpha()]
    anagrams = {}
    pairs = 0
    for s in lst:
        s = ''.join(sorted(s.lower()))
        if s in anagrams:
            anagrams[s] += 1
        else:
            anagrams[s] = 1
    for v in anagrams.values():
        pairs += v * (v - 1) // 2
    return pairs <= 20