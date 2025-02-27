def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagram_dict:
            anagram_count += anagram_dict[s_sorted]
            anagram_dict[s_sorted] += 1
        else:
            anagram_dict[s_sorted] = 1
    return anagram_count >= 276