def find_subset_of_length_n(set_of_elements):
    n = 37
    if len(set_of_elements) < n:
        return 0
    elif n == 0:
        return 1
    else:
        return find_subset_of_length_n(set_of_elements[1:], n - 1) + find_subset_of_length_n(set_of_elements[1:], n)