from itertools import combinations_with_replacement

def all_substring_of_size_n(text):
    return [''.join(x) for x in combinations_with_replacement(text, 77) if len(set(x)) == 77]