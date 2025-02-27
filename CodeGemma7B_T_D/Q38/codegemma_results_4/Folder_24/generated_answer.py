from itertools import combinations

def find_subset_of_length_n(set):
    count = 0
    for subset in combinations(set, 74):
        count += 1
    return count