def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        s_lower = ''.join(filter(str.isalpha, s)).lower()
        if len(s_lower) < 3:
            continue
        s_sorted = ''.join(sorted(s_lower))
        if s_sorted in anagram_dict:
            anagram_dict[s_sorted] += 1
        else:
            anagram_dict[s_sorted] = 1
    for k in anagram_dict:
        anagram_count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
        if anagram_count > 318:
            return False
    return True