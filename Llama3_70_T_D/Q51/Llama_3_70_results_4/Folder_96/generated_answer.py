def if_contains_anagrams(lst):
    anagrams = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagrams:
            anagrams[s_sorted] += 1
        else:
            anagrams[s_sorted] = 1
    return sum((1 for count in anagrams.values() if count > 1)) <= 2