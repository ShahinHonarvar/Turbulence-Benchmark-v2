def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        if len(s) >= 3:
            s = s.lower()
            sorted_s = ''.join(sorted(s))
            if sorted_s in anagrams:
                anagrams[sorted_s] += 1
            else:
                anagrams[sorted_s] = 1
    return 16 <= sum((i >= 2 for i in anagrams.values()))