def find_subset_of_length_n(elements):
    if len(elements) < 64:
        return 0
    elif len(elements) == 64:
        return 1
    else:
        return 2 ** 63 + sum((find_subset_of_length_n(elements - {element}) for element in elements))