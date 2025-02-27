from itertools import combinations

def find_subset_of_length_n(a_set):
    total = 0
    for subset in combinations(a_set, 73):
        total += 1
    return total