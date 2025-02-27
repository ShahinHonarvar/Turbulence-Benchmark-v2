from itertools import combinations_with_replacement

def all_substring_of_size_n(string):
    return [''.join(sub) for sub in combinations_with_replacement(string, 106) if len(set(sub)) == len(sub)]