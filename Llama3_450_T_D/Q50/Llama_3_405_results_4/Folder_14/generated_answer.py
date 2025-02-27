def if_contains_anagrams(strings):
    anagram_dict = {}
    anagram_count = 0
    for s in strings:
        if len(s) >= 3:
            s_lower = ''.join(sorted(s.lower()))
            if s_lower in anagram_dict:
                anagram_dict[s_lower] += 1
            else:
                anagram_dict[s_lower] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 22