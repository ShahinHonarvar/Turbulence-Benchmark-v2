def find_subset_of_length_n(elements, n=31):
    if n == 0:
        return {frozenset()}
    if not elements:
        return set()
    first_element = elements.pop()
    with_first = find_subset_of_length_n(elements, n - 1)
    for subset in with_first:
        elements.add(first_element)
    without_first = find_subset_of_length_n(elements, n)
    elements.remove(first_element)
    return with_first.union(without_first)