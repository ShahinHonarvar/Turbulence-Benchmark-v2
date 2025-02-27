def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s_lower) >= 3:
            anagram_dict[sorted_str] = anagram_dict.get(sorted_str, 0) + 1
    anagram_count = sum((i * (i - 1) // 2 for i in anagram_dict.values() if i > 1))
    return anagram_count <= 173