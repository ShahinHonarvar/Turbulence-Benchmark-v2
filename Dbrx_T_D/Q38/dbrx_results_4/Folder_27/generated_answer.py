def find_subset_of_length_n(element_set, n=56):
    if n > len(element_set) or n < 0:
        return 0
    elif n == 0:
        return 1
    else:
        return sum((find_subset_of_length_n(element_set - {element}, n - 1) for element in element_set))