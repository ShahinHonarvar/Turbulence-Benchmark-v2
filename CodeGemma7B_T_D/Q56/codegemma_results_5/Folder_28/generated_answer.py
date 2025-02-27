from itertools import combinations_with_replacement

def all_substring_of_size_n(str):
    char_list = list(str)
    return [''.join(c) for c in combinations_with_replacement(char_list, 44)]