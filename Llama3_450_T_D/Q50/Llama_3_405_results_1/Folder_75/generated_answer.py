def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s_lower = s.lower()
        sorted_str = ''.join(sorted(s_lower))
        if len(s) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s_lower)
            else:
                anagram_dict[sorted_str] = [s_lower]
    for key in anagram_dict:
        if len(anagram_dict[key]) > 1:
            count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
        if count >= 70:
            return True
    return False