def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    anagram_count = 0
    for count in anagram_dict.values():
        anagram_count += count * (count - 1) // 2
    return anagram_count >= 106