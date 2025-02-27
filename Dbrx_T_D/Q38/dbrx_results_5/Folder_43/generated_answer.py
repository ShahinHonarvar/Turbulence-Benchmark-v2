def find_subset_of_length_n(set_elements, n=29):
    length_of_subset = n
    set_elements = list(set_elements)
    if length_of_subset > len(set_elements) or length_of_subset < 0:
        return 'Error: Argument n out of range [0, len(set_elements)]'
    if length_of_subset == 0 or length_of_subset == len(set_elements):
        return 1
    return len(list(itertools.combinations(set_elements, length_of_subset)))