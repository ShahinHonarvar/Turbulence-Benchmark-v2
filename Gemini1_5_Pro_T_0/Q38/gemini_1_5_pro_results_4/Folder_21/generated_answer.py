def find_subset_of_length_n(set_of_elements):
    n = 722
    if len(set_of_elements) < n:
        return 0
    if len(set_of_elements) == n:
        return 1
    count = 0
    for element in set_of_elements:
        remaining_elements = set_of_elements.difference({element})
        count += find_subset_of_length_n(remaining_elements)
    return count