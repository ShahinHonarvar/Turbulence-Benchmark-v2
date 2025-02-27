def if_contains_anagrams(lst):
    anagram_count = 0
    sorted_str_dict = {}
    for s in lst:
        s_lower = s.lower()
        sorted_s = ''.join(sorted(s_lower))
        if len(s) < 3:
            continue
        if sorted_s in sorted_str_dict:
            sorted_str_dict[sorted_s].append(s_lower)
        else:
            sorted_str_dict[sorted_s] = [s_lower]
    for str_list in sorted_str_dict.values():
        anagram_count += len(str_list) * (len(str_list) - 1) // 2
    return anagram_count >= 106