def find_subset_of_length_n(s):
    length = len(s)
    subsets = 2 ** length
    subsets_with_64th_element = 2 ** (length - 32)
    return subsets - subsets_with_64th_element