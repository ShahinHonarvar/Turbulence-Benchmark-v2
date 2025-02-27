def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s_lower)
        else:
            anagram_dict[sorted_str] = [s_lower]
    for value in anagram_dict.values():
        anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count >= 86