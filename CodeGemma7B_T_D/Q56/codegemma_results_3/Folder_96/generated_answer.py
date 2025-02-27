from itertools import combinations_with_replacement, permutations

def all_substring_of_size_n(string):
    return list(map(lambda p: ''.join(p), permutations(combinations_with_replacement(string, 21), n=string.__len__())))