from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        str_dict[sorted_str].append(string)
    anagram_pairs = sum((len(group) * (len(group) - 1) // 2 for group in str_dict.values() if len(group) > 1))
    return anagram_pairs <= 173