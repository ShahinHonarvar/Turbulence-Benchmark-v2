def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s_lower = ''.join(sorted(s.lower()))
        if len(s) >= 3 and s_lower.isalpha():
            if s_lower in anagram_dict:
                anagram_dict[s_lower] += 1
            else:
                anagram_dict[s_lower] = 1
    count = 0
    for k in anagram_dict:
        count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
        if count > 47:
            return False
    return True