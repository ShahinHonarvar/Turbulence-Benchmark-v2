def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        if len(s) < 3:
            continue
        s_lower = ''.join(sorted(s.lower()))
        if s_lower in anagram_dict:
            anagram_dict[s_lower].append(s)
        else:
            anagram_dict[s_lower] = [s]
    anagram_count = 0
    for v in anagram_dict.values():
        anagram_count += len(v) * (len(v) - 1) // 2
    return anagram_count >= 35