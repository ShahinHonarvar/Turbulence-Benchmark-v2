def if_contains_anagrams(lst):
    lst = [s.lower() for s in lst if len(s) >= 3]
    anagrams = {}
    for s in lst:
        sorted_s = ''.join(sorted(s))
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    pairs = 0
    for count in anagrams.values():
        pairs += count * (count - 1) // 2
    return pairs >= 277