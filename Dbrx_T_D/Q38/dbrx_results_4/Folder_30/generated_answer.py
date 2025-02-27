def find_subset_of_length_n(set_elements, n):
    if n == 1:
        return {frozenset([element]) for element in set_elements}
    else:
        return {frozenset(subset | {element}) for element in set_elements for subset in find_subset_of_length_n(set_elements, n - 1)}