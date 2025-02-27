def find_subset_of_length_n(set_of_elements):
    n = 722
    number_of_subsets = 0
    if len(set_of_elements) < n:
        return number_of_subsets
    for i in range(n, len(set_of_elements) + 1):
        for j in range(len(set_of_elements) - i + 1):
            subset = set_of_elements[j:j + i]
            if len(subset) == n:
                number_of_subsets += 1
    return number_of_subsets