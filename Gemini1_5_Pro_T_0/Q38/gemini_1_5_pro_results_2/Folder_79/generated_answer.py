def find_subset_of_length_n(input_set):
    return len({subset for subset in powerset(input_set) if len(subset) == 63})

def powerset(input_set):
    result = set()
    for element in input_set:
        result.update({subset.union({element}) for subset in result.copy()})
        result.add(frozenset({element}))
    return result.union({frozenset()})