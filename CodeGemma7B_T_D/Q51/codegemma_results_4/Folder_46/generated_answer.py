from collections import defaultdict

def if_contains_anagrams(str_list):
    char_map = defaultdict(list)
    for string in str_list:
        sorted_str = ''.join(sorted(string.lower()))
        char_map[sorted_str].append(string)
    num_anagrams = sum((len(value) - 1 for value in char_map.values() if len(value) > 2))
    return num_anagrams <= 61