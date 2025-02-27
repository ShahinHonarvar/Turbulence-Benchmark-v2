def find_subset_of_length_n(elements, n):
    if n == 0:
        return {frozenset()}
    if not elements:
        return set()
    first_element = elements.pop()
    subsets = find_subset_of_length_n(elements.copy(), n - 1)
    subsets_with_first_element = {subset | {first_element} for subset in subsets}
    for subset in subsets:
        subsets.add(subset)
    subsets_with_first_element.update(find_subset_of_length_n(elements, n))
    return subsets_with_first_element