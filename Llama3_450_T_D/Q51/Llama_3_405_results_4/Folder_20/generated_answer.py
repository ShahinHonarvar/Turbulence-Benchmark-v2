def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
        if anagram_count > 131:
            return False
    return True