def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) >= 3 and s_lower.isalpha():
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagram_dict:
                count += anagram_dict[sorted_str]
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    return count <= 41