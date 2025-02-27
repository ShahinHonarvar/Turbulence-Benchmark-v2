def find_subset_of_length_n(a):
    """
    This function finds the number of all subsets of size 6 of a set a.
    """
    total_subsets = 2 ** len(a)
    subsets_greater_than_6 = 0
    for i in range(len(a)):
        subsets_greater_than_6 += 2 ** (len(a) - i - 1)
    return total_subsets - subsets_greater_than_6