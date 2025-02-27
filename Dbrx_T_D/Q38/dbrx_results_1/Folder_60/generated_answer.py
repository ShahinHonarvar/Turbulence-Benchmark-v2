def find_subset_of_length_n(element_set, n):
    if n == 0:
        return {frozenset()}
    if not element_set:
        return set()
    first_element = element_set.pop()
    subsets = find_subset_of_length_n(element_set, n - 1)
    for subset in find_subset_of_length_n(element_set, n):
        subsets.add(subset | frozenset(first_element))
    element_set.add(first_element)
    return subsets

def count_subsets_of_length_n(element_set, n):
    return len(find_subset_of_length_n(element_set, n))