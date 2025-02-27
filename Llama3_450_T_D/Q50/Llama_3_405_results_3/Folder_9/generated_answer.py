def if_contains_anagrams(string_list):
    anagram_dict = {}
    count = 0
    for s in string_list:
        if len(s) < 3:
            continue
        sorted_str = ''.join(sorted(s.lower()))
        if sorted_str in anagram_dict:
            anagram_dict[sorted_str] += 1
        else:
            anagram_dict[sorted_str] = 1
    for key in anagram_dict:
        if anagram_dict[key] > 1:
            count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return count >= 66