def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(s) >= 3:
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str].append(s)
            else:
                anagram_dict[sorted_str] = [s]
    anagram_count = 0
    for key in anagram_dict:
        anagram_count += len(anagram_dict[key]) * (len(anagram_dict[key]) - 1) // 2
    return anagram_count >= 95