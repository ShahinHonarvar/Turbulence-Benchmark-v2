from collections import defaultdict

def if_contains_anagrams(str_list):
    str_dict = defaultdict(list)
    for string in str_list:
        sorted_string = ''.join(sorted(string.lower()))
        str_dict[sorted_string].append(string)
    count = 0
    for group in str_dict.values():
        if len(group) > 2:
            count += len(group) - 1
    return count <= 60