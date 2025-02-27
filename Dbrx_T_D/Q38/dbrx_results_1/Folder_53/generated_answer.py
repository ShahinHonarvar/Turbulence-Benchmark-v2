def find_subset_of_length_n(element_set):
    if len(element_set) < 73:
        return 0
    if len(element_set) == 73:
        return 1
    count = 0
    for i in range(len(element_set) - 72):
        subset = element_set - {list(element_set)[i]}
        count += find_subset_of_length_n(subset)
    return count