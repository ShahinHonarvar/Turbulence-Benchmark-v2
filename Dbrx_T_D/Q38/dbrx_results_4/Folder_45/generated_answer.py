def find_subset_of_length_n(element_set):
    if len(element_set) < 33:
        return 0
    if len(element_set) == 33:
        return 1
    return sum((find_subset_of_length_n(s) for s in subsets_of_size(element_set, 33)))

def subsets_of_size(element_set, size):
    if size == 0:
        return {frozenset()}
    if not element_set:
        return set()
    first_element = element_set.pop()
    with_first = {s.union({first_element}) for s in subsets_of_size(element_set, size - 1)}
    without_first = subsets_of_size(element_set, size)
    return with_first.union(without_first)