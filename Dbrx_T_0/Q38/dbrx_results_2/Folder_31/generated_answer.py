def find_subset_of_length_n(elements, n):
    if n == 0:
        return {frozenset()}
    if not elements:
        return set()
    first_element = elements.pop()
    subsets = find_subset_of_length_n(elements, n - 1)
    for subset in find_subset_of_length_n(elements, n):
        subsets.add(frozenset(subset | {first_element}))
    return subsets

def count_subsets_of_length_n(elements, n):
    return len(find_subset_of_length_n(elements, n))