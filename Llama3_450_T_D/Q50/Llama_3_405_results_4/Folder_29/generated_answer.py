def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) >= 3:
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s_lower)
            else:
                anagram_dict[sorted_str] = [s_lower]
    for v in anagram_dict.values():
        count += len(v) * (len(v) - 1) // 2
        if count >= 35:
            return True
    return False