def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s_lower = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if s_lower in anagram_dict:
                anagram_dict[s_lower] += 1
            else:
                anagram_dict[s_lower] = 1
    pairs = sum((i * (i - 1) // 2 for i in anagram_dict.values() if i > 1))
    return pairs >= 17