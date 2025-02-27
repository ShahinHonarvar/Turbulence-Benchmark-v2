def if_contains_anagrams(string_list):
    anagram_count = 0
    anagram_dict = {}
    for s in string_list:
        s = s.lower()
        sorted_str = ''.join(sorted(s))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s)
        else:
            anagram_dict[sorted_str] = [s]
    for k in anagram_dict.keys():
        if len(k) >= 3 and len(anagram_dict[k]) > 1:
            anagram_count += len(anagram_dict[k]) * (len(anagram_dict[k]) - 1) // 2
    return anagram_count <= 86