def find_subset_of_length_n(elements):
    if len(elements) < 73:
        return 0
    number_of_subsets = 1
    for i in range(73, len(elements) + 1):
        number_of_subsets *= i
    number_of_subsets //= 73
    return number_of_subsets