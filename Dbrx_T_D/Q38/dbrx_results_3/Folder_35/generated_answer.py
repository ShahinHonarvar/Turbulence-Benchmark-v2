def find_subset_of_length_n(elements_set):
    if len(elements_set) < 300:
        return 0
    elif len(elements_set) == 300:
        return 1
    else:
        return find_subset_of_length_n(set(elements_set.pop())) + find_subset_of_length_n(elements_set | {elements_set.pop()})