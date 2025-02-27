def find_subset_of_length_n(elements: set, n: int) -> int:
    if n < 0 or not elements:
        return 0
    elif n == 0:
        return 1
    elif len(elements) == n:
        return 1 if set(elements) == elements else 0
    else:
        return find_subset_of_length_n(elements - {elements.pop()}, n) + find_subset_of_length_n(elements, n)