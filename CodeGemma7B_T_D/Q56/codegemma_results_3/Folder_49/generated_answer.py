from itertools import combinations_with_replacement

def all_substring_of_size_n(text):
    length = 73
    return [''.join(i) for i in combinations_with_replacement(text, length)]