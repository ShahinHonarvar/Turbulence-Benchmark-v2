def find_subset_of_length_n(elements, n):
    if n == 0:
        return 1
    if not elements:
        return 0
    with_first = find_subset_of_length_n(elements - {elements.pop()}, n - 1)
    without_first = find_subset_of_length_n(elements, n)
    return with_first + without_first