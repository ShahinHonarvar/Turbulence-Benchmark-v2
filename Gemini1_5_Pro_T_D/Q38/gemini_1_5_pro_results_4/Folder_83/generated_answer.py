def find_subset_of_length_n(set_of_elements):
    n = 95
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return 0
    elif len(set_of_elements) == n:
        return 1
    else:
        number_of_subsets = 1
        for i in range(n):
            number_of_subsets = number_of_subsets * (len(set_of_elements) - i) // (i + 1)
        return number_of_subsets