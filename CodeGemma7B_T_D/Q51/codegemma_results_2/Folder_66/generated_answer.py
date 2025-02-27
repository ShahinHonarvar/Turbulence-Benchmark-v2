def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string not in anagram_dict:
            anagram_dict[sorted_string] = []
        anagram_dict[sorted_string].append(string)
    num_anagrams = 0
    for anagram_group in anagram_dict.values():
        num_anagrams += len(anagram_group) * (len(anagram_group) - 1) // 2
    return num_anagrams <= 64