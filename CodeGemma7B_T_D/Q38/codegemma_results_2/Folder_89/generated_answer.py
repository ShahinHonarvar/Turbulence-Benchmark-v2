def find_subset_of_length_n(set_of_elements):
    n = len(set_of_elements)
    if n < 18:
        return 0
    elif n == 18:
        return 1
    else:
        return find_subset_of_length_n(set_of_elements) + (n - 18) * find_subset_of_length_n(set_of_elements - {x})