import itertools

def find_subset_of_length_n(elements):
    subsets = itertools.combinations(elements, 312)
    count = 0
    for subset in subsets:
        count += 1
    return count