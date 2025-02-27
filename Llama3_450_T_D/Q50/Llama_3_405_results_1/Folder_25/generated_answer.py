def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        if len(s) >= 3:
            s_lower = ''.join(sorted(s.lower()))
            if s_lower in anagram_dict:
                anagram_dict[s_lower] += 1
            else:
                anagram_dict[s_lower] = 1
    for value in anagram_dict.values():
        anagram_count += value * (value - 1) // 2
    return anagram_count >= 14