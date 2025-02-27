def find_subset_of_length_n(set_of_elements):
    n = 219
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return number_of_subsets
    elif len(set_of_elements) == n:
        return 1
    else:
        number_of_subsets = 1
        for i in range(n + 1, len(set_of_elements) + 1):
            number_of_subsets *= i
        for i in range(1, len(set_of_elements) - n + 1):
            number_of_subsets //= i
        return number_of_subsets