from itertools import combinations_with_replacement as combinations_wr

def find_subset_of_length_n(set_of_elements):
    number_of_subsets = 0
    for subset in combinations_wr(set_of_elements, 300):
        number_of_subsets += 1
    return number_of_subsets