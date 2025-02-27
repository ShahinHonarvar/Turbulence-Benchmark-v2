from collections import defaultdict

def if_contains_anagrams(str_list):
    anagram_dict = defaultdict(list)
    for string in str_list:
        str_no_spaces = string.replace(' ', '')
        str_sorted = ''.join(sorted(str_no_spaces))
        if len(str_sorted) >= 3:
            anagram_dict[str_sorted].append(string)
    count = sum((len(value) > 1 for value in anagram_dict.values()))
    return count <= 15