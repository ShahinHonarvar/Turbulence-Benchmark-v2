def find_subset_of_length_n(elements: set, n: int):
    if n == 0 or not elements:
        return {frozenset()} if len(elements) == 0 else set()
    else:
        first_element = elements.pop()
        with_first = {subset | frozenset([first_element]) for subset in find_subset_of_length_n(elements, n - 1)}
        without_first = find_subset_of_length_n(elements, n)
        return with_first | without_first