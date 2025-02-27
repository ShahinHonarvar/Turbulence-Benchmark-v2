def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        if len(s) < 3:
            continue
        s_lower = ''.join(sorted(s.lower()))
        if s_lower in anagram_dict:
            anagram_dict[s_lower] += 1
        else:
            anagram_dict[s_lower] = 1
    count = 0
    for value in anagram_dict.values():
        count += value * (value - 1) // 2
        if count > 19:
            return False
    return True