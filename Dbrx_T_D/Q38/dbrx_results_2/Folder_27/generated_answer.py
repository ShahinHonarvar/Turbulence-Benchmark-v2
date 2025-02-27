def find_subset_of_length_n(elements: set, n: int) -> int:
    if n < 0 or len(elements) < n:
        return 0
    if n == 0 or n == len(elements):
        return 1
    with_elements = find_subset_of_length_n(elements - {elements.pop()}, n)
    without_elements = find_subset_of_length_n(elements, n - 1)
    return with_elements + without_elements