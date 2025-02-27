from itertools import combinations

def find_subset_of_length_n(set):
    size = 63
    count = 0
    for s in combinations(set, size):
        count += 1
    return count