def if_contains_anagrams(string_list):
    anagram_dict = {}
    anagram_count = 0
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) < 3:
            continue
        sorted_s = ''.join(sorted(s_lower))
        if sorted_s in anagram_dict:
            anagram_dict[sorted_s] += 1
        else:
            anagram_dict[sorted_s] = 1
    for key in anagram_dict:
        anagram_count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return anagram_count >= 194