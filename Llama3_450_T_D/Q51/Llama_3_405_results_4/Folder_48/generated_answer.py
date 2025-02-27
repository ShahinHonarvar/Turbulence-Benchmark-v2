def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s_lower) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for k in anagram_dict:
        count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
        if count > 277:
            return False
    return True