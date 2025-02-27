def if_contains_anagrams(strings):
    sorted_strings = [''.join(sorted(s.lower())) for s in strings if len(s) >= 3]
    anagram_map = {}
    for s in sorted_strings:
        if s in anagram_map:
            anagram_map[s] += 1
        else:
            anagram_map[s] = 1
    anagram_count = sum((count * (count - 1) // 2 for count in anagram_map.values()))
    return anagram_count >= 233