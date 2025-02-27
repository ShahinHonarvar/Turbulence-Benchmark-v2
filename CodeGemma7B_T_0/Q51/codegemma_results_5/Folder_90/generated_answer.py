def if_contains_anagrams(str_list):
    anagram_dict = {}
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) < 3:
            continue
        if sorted_string in anagram_dict:
            anagram_dict[sorted_string] += 1
        else:
            anagram_dict[sorted_string] = 1
    return len(anagram_dict) <= 147