def find_subset_of_length_n(elements, n):
    if n == 0:
        return {frozenset()}
    if not elements:
        return set()
    element = elements.pop()
    with_element = find_subset_of_length_n(elements, n - 1)
    with_element = {s | {element} for s in with_element}
    without_element = find_subset_of_length_n(elements, n)
    return with_element | without_element