def find_subsets_of_length_n(elements, n):
    if n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return len(elements) * find_subsets_of_length_n(elements, n - 1)