def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        sorted_s = ''.join(sorted(s_lower))
        if len(sorted_s) >= 3:
            if sorted_s in anagram_dict:
                anagram_dict[sorted_s] += 1
            else:
                anagram_dict[sorted_s] = 1
    for k in anagram_dict:
        count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
        if count > 24:
            return False
    return True