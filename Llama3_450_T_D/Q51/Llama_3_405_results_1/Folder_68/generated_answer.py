def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        s_lower = s.lower()
        if len(s_lower) < 3 or not s_lower.isalpha():
            continue
        sorted_str = ''.join(sorted(s_lower))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str].append(s_lower)
        else:
            anagram_dict[sorted_str] = [s_lower]
    anagram_count = 0
    for value in anagram_dict.values():
        anagram_count += len(value) * (len(value) - 1) // 2
    return anagram_count <= 94