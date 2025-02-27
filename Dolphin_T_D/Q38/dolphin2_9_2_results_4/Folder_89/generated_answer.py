def find_subset_of_length_n(set_elements):
    if not set_elements:
        return 0
    if len(set_elements) < 18:
        return 0
    elif len(set_elements) == 18:
        return 1
    else:
        return len(set_elements) * find_subset_of_length_n(set_elements - set_elements.pop()) + 1