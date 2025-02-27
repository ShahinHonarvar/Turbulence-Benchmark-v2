def if_contains_anagrams(strings):
    anagram_map = {}
    for s in strings:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s) >= 3:
            if sorted_str in anagram_map:
                anagram_map[sorted_str].append(s)
            else:
                anagram_map[sorted_str] = [s]
    anagram_count = 0
    for value in anagram_map.values():
        if len(value) > 1:
            anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count >= 46