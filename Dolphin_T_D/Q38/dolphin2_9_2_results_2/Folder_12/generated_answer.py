from itertools import combinations

def find_subset_of_length_27(s):
    return len(list(combinations(s, 27)))