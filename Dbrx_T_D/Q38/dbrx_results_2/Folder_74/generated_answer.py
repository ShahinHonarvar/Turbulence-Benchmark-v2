def find_subset_of_length_n(elements: set, n: int) -> int:
    if n < 0 or (len(elements) < n and (not elements)):
        return 0
    if n == 0 or n == len(elements):
        return 1
    else:
        return find_subset_of_length_n(elements - {elements.pop()}, n - 1) + find_subset_of_length_n(elements, n)