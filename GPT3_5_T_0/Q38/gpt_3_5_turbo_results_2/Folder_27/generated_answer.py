import itertools

def find_subset_of_length_n(elements):
    count = 0
    for subset in itertools.combinations(elements, 56):
        count += 1
    return count