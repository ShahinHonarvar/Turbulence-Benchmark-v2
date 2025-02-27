from itertools import combinations

def all_substring_of_size_n(string):
    len_str = len(string)
    list_of_combinations = list(combinations(string, 117))
    return list(set([''.join(sublist) for sublist in list_of_combinations]))