def find_subset_of_length_n(n, elements):
    if n != 54 or not elements:
        return 0
    if len(elements) == 54:
        return 1
    return sum((find_subset_of_length_n(n - 1, elements - {element}) for element in elements))