def find_subset_of_length_n(elements_set):
    if len(elements_set) < 76:
        return 0
    elif len(elements_set) == 76:
        return 1
    else:
        return sum((find_subset_of_length_n(subset) for subset in subsets_of_size(elements_set, 76)))

def subsets_of_size(elements_set, size):
    if size == 0:
        return {frozenset()}
    elif size < 0:
        return set()
    else:
        return {subset | {element} for element in elements_set for subset in subsets_of_size(elements_set - {element}, size - 1)}