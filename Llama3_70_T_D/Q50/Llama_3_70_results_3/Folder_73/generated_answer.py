def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s].append(s_lower)
        else:
            anagram_dict[sorted_s] = [s_lower]
    for v in anagram_dict.values():
        anagram_count += len(v) * (len(v) - 1) // 2
    return anagram_count >= 91