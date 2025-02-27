def find_subset_of_length_n(set_of_elements):
    if len(set_of_elements) < 40:
        return 0
    elif len(set_of_elements) == 40:
        return 1
    else:
        subset_count = 0
        for i in range(len(set_of_elements) - 39):
            subset_count += find_subset_of_length_n(set_of_elements.difference(set_of_elements[i]))
        return subset_count