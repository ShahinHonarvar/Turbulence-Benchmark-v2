def if_contains_anagrams(lst):
    anagrams_count = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s.lower()))
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagrams_count:
            anagrams_count[sorted_s] += 1
        else:
            anagrams_count[sorted_s] = 1
    return sum((n * (n - 1) // 2 for n in anagrams_count.values())) <= 81