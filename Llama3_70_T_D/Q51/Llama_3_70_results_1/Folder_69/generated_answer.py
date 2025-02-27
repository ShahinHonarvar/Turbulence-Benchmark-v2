def if_contains_anagrams(lst):
    anagram_map = {}
    for s in lst:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(s_lower)
        else:
            anagram_map[sorted_str] = [s_lower]
    return sum((len(val) * (len(val) - 1) // 2 for val in anagram_map.values())) <= 58