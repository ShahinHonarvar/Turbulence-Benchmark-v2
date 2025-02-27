import itertools

def find_subset_of_length_n(set1):
    i = 0
    for set_n in itertools.combinations(set1, 45):
        i += 1
    return i