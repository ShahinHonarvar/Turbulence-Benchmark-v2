import itertools

def find_subset_of_length_n(set):
    count = 0
    for subset in itertools.combinations(set, 793):
        count += 1
    return count