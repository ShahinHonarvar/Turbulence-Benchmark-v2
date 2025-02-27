def find_subset_of_length_n(elements, n):
    return sum((width * combinations(elements, n)[width - 1] for width in range(1, len(elements) + 1)))