def find_subset_of_length_n(element_set, n=57):
    if n == 0:
        return 1
    elif len(element_set) == 0:
        return 0
    else:
        return find_subset_of_length_n(element_set - {element_set[-1]}, n - 1) + find_subset_of_length_n(element_set - {element_set[-1]}, n)