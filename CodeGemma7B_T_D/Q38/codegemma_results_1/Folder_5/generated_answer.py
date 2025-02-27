def find_subsets_of_length_n(my_set, element_count):
    """
    This function will return the number of all subsets of a set of elements of a given size.
    """
    num_subsets = len(my_set) ** element_count
    return num_subsets