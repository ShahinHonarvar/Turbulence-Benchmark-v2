from itertools import combinations_with_replacement

def all_substring_of_size_n(str):
    length = 12
    return sorted([''.join(i) for i in combinations_with_replacement(str, length)])