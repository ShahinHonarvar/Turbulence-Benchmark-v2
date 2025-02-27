from itertools import combinations as combinaciones

def find_subset_of_length_n(set_of_elements, n=449):
    return len(list(filter(lambda subset: len(subset) == n, combinaciones(set_of_elements, n))))