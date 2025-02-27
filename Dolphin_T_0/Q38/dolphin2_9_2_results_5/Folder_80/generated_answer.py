def find_subset_of_length_n(elements, n=36):
    if n == 0:
        return 1
    if len(elements) == 0:
        return 0
    return find_subset_of_length_n(elements[1:], n) + find_subset_of_length_n(elements[1:], n - 1)