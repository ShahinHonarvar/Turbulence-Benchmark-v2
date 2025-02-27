def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        if len(s) >= 3 and s.isalpha():
            sorted_str = ''.join(sorted(s.lower()))
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    count = 0
    for key in anagram_dict:
        count += anagram_dict[key] * (anagram_dict[key] - 1) // 2
    return count <= 474