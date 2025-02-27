def if_contains_anagrams(lst):
    anagrams = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        sorted_s = ''.join(sorted((c for c in s_lower if c.isalpha())))
        if len(sorted_s) < 3:
            continue
        if sorted_s in anagrams:
            anagrams[sorted_s] += 1
        else:
            anagrams[sorted_s] = 1
    for v in anagrams.values():
        count += v * (v - 1) // 2
    return count <= 48