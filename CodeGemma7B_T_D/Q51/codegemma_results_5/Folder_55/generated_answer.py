from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    anagram_count = 0
    for string in str_list:
        string = ''.join(sorted(string.lower()))
        if len(string) >= 3:
            str_dict[string].append(string)
    for anagram_list in str_dict.values():
        anagram_count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return anagram_count <= 44