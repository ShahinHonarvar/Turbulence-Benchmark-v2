import itertools

def find_subset_of_length_n(set_elements):
    count = 0
    for subset in itertools.combinations(set_elements, 63):
        count += 1
    return count