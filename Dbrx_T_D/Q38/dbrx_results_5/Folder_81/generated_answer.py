def find_subset_of_length_n(elements_set):
    if len(elements_set) < 20:
        return 0
    else:
        return (len(elements_set) - 19) * find_subset_of_length_n(elements_set.difference({elements_set.pop()}))