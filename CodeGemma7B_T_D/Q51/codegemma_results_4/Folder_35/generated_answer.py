from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        str_dict[sorted_string].append(string)
    return len(str_dict) <= 210