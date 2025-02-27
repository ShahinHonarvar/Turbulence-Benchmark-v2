def find_subset_of_length_n(set_of_elements):
    n = 894
    number_of_elements = len(set_of_elements)
    if n > number_of_elements:
        return 0
    if n == 0 or n == number_of_elements:
        return 1
    if n == 1:
        return number_of_elements
    return find_subset_of_length_n(set_of_elements[1:], n - 1) + find_subset_of_length_n(set_of_elements[1:], n)