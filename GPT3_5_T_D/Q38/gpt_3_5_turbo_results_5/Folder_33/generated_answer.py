from itertools import combinations

def find_subset_of_length_n(elements):
    subsets = combinations(elements, 372)
    count = 0
    for subset in subsets:
        count += 1
    return count