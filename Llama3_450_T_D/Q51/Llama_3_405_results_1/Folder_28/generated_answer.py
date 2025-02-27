def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) >= 3 and s_lower.isalpha():
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
        if count > 78:
            return False
    return True