def if_contains_anagrams(strs):
    anagram_map = {}
    anagram_count = 0
    for s in strs:
        s = s.casefold()
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagram_map:
            anagram_map[sorted_str].append(s)
        else:
            anagram_map[sorted_str] = [s]
    for value in anagram_map.values():
        n = len(value)
        anagram_count += n * (n - 1) // 2
    return anagram_count >= 61