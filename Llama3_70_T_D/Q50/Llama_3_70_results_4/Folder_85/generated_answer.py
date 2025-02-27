def if_contains_anagrams(lst):
    anagram_map = {}
    count = 0
    for s in lst:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_map:
            anagram_map[sorted_s].append(s_lower)
        else:
            anagram_map[sorted_s] = [s_lower]
    for v in anagram_map.values():
        n = len(v)
        count += n * (n - 1) // 2
    return count >= 73