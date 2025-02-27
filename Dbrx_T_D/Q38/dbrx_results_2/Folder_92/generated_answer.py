def find_subset_of_length_n(elements_set, n=0):
    if n == 0:
        return {frozenset()}
    if not elements_set:
        return set()
    first_element = elements_set.pop()
    with_first = {subset | {first_element} for subset in find_subset_of_length_n(elements_set, n - 1)}
    without_first = find_subset_of_length_n(elements_set, n)
    return with_first | without_first