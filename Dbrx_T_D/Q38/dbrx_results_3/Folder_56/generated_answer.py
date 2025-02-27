def find_subset_of_length_n(element_set, n):
    if n == 0:
        return {frozenset()}
    if not element_set:
        return set()
    element, rest = (element_set.copy(), element_set.copy())
    element.pop()
    rest.remove(element)
    return {subset | {element} for subset in find_subset_of_length_n(rest, n - 1)} | find_subset_of_length_n(rest, n)