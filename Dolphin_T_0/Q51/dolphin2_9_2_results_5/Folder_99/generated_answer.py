import collections
import itertools

def if_contains_anagrams(string_list):
    string_dict = {}
    for string in string_list:
        string_dict[string.lower()[:3] + string.lower()[-3:]] = string.lower()
    for values in string_dict.values():
        if list(values) != sorted(list(values)):
            return True
    return False