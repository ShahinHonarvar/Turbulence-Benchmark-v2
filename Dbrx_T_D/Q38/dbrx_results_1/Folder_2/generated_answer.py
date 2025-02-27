def find_subset_of_length_n(element_set):
    total_subsets = 0
    if len(element_set) >= 616:
        for i in range(len(element_set) - 615):
            total_subsets += 1
    else:
        return 0
    return total_subsets