def find_subset_of_length_n(element_set):
    if len(element_set) < 180:
        return 0
    if len(element_set) == 180:
        return 1
    return sum([find_subset_of_length_n(element_set.difference({element})) for element in element_set])