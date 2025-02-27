def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(sorted_str) >= 3:
            if sorted_str in anagram_dict:
                anagram_count += anagram_dict[sorted_str]
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    return anagram_count <= 475