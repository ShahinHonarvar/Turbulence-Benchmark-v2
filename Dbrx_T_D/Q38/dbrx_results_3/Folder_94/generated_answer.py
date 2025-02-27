def find_subset_of_length_n(elements_set, n):
    if n == 0:
        return [[]]
    subsets = []
    for element in elements_set:
        for subset in find_subset_of_length_n(elements_set - {element}, n - 1):
            subsets.append(subset + [element])
    return subsets

def find_subset_count_of_length_n(elements_set, n):
    return len(find_subset_of_length_n(elements_set, n))