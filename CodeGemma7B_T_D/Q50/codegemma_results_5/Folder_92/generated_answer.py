from collections import defaultdict

def if_contains_anagrams(string_list):
    string_dict = defaultdict(list)
    for string in string_list:
        sorted_string = ''.join(sorted(string.lower()))
        if len(sorted_string) >= 3:
            string_dict[sorted_string].append(string)
    for group in string_dict.values():
        if len(group) >= 2:
            return True
    return False