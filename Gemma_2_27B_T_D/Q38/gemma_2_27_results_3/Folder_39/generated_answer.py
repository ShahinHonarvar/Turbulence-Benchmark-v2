def find_subset_of_length_n(elements):
    n = 59
    total_subsets = 2 ** len(elements)
    return int(total_subsets / 2 ** n)