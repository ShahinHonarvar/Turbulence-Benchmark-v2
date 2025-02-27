def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) >= 3 and s_lower.isalpha():
            sorted_str = ''.join(sorted(s_lower))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s_lower)
            else:
                anagram_dict[sorted_str] = [s_lower]
    anagram_count = 0
    for k in anagram_dict:
        anagram_count += len(anagram_dict[k]) * (len(anagram_dict[k]) - 1) // 2
    return anagram_count <= 116