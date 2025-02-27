def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s)
        else:
            anagram_dict[sorted_str] = [s]
    anagram_count = 0
    for k, v in anagram_dict.items():
        if len(k) >= 3 and len(v) > 1:
            anagram_count += len(v) * (len(v) - 1) // 2
    return anagram_count >= 189