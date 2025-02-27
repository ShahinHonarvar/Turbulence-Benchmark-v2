from collections import defaultdict

def if_contains_anagrams(list_of_strings):
    str_map = defaultdict(list)
    for string in list_of_strings:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            str_map[sorted_string].append(string)
    return len(str_map) <= 41