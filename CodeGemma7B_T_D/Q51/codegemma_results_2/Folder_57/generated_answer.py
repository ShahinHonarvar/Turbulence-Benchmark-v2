from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        str_dict[''.join(sorted(string.lower()))].append(string)
    count = 0
    for anagram_list in str_dict.values():
        if len(anagram_list) >= 3:
            count += len(anagram_list) * (len(anagram_list) - 1) // 2
    return count <= 74