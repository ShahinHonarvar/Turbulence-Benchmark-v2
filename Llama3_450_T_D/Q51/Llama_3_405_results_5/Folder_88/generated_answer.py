def if_contains_anagrams(string_list):
    anagram_dict = {}
    for s in string_list:
        sorted_str = ''.join(sorted(s.lower()))
        if len(sorted_str) >= 3 and sorted_str.isalpha():
            if sorted_str in anagram_dict:
                anagram_dict[sorted_str] += 1
            else:
                anagram_dict[sorted_str] = 1
    anagram_count = 0
    for k in anagram_dict:
        anagram_count += anagram_dict[k] * (anagram_dict[k] - 1) // 2
    return anagram_count <= 407