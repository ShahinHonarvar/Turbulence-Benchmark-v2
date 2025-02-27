def find_subset_of_length_n(elements_set, n):
    if n < 0 or not isinstance(elements_set, set) or (not all((isinstance(elem, str) for elem in elements_set))):
        return 'Input validation error. Please provide a set of strings and a non-negative integer as arguments.'
    if n == 0:
        return {frozenset()}
    if not elements_set:
        return set()
    first_element = elements_set.pop()
    with_first = find_subset_of_length_n(elements_set, n - 1)
    for subset in list(with_first):
        with_first.remove(subset)
        with_first.add(subset | {first_element})
    without_first = find_subset_of_length_n(elements_set, n)
    return with_first | without_first