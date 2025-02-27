def find_subset_of_length_n(elements_set, n):
    if n < 0 or not isinstance(elements_set, set) or (not all((isinstance(el, int) or isinstance(el, float) for el in elements_set))):
        raise ValueError('Incorrect input. Please provide a set of elements and the size of the subset.')
    if n == 0:
        return {frozenset()}
    if not elements_set:
        return set()
    first_elt = elements_set.pop()
    subsets_with_first_elt = {frozenset(subset.union({first_elt})) for subset in find_subset_of_length_n(elements_set, n - 1)}
    subsets_without_first_elt = find_subset_of_length_n(elements_set, n)
    return subsets_with_first_elt.union(subsets_without_first_elt)