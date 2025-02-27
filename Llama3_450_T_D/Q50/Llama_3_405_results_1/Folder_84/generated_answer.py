def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        if len(s) >= 3:
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    for k, v in anagram_dict.items():
        count += v * (v - 1) // 2
        if count >= 108:
            return True
    return False