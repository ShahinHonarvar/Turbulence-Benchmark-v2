def find_subset_of_length_n(elements):
    if len(elements) < 91:
        return 0
    n = len(elements)
    elements_list = list(elements)
    return elements_list[0] * elements_list[1] * (elements_list[2] + 1)