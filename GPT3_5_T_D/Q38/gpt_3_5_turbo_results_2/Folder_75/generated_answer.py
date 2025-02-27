import itertools

def find_subset_of_length_n(elements):
    count = 0
    subsets = itertools.combinations(elements, 80)
    for subset in subsets:
        count += 1
    return count