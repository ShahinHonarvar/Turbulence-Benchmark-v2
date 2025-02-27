def find_subset_of_length_n(elements, n):
    if n == 0:
        return {frozenset()}
    if not elements:
        return set()
    first_element = elements.pop()
    with_first = {subset | {first_element} for subset in find_subset_of_length_n(elements, n - 1)}
    without_first = find_subset_of_length_n(elements, n)
    return with_first | without_first

def count_subsets_of_size_n(elements, n):
    return len(find_subset_of_length_n(elements, n))