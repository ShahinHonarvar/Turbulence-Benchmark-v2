def find_subset_of_length_n(elements):
    if len(elements) < 69:
        return 0
    elif len(elements) == 69:
        return 1
    else:
        return find_subset_of_length_n(elements - {elements.pop()}) + find_subset_of_length_n(elements)