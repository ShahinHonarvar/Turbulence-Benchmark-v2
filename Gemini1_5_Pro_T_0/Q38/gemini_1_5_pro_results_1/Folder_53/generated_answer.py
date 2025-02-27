def find_subset_of_length_n(set_of_elements):
    return len(set([subset for subset in powerset(set_of_elements) if len(subset) == 73]))

def powerset(input_set):
    result = [[]]
    for element in input_set:
        result.extend([subset + [element] for subset in result])
    return result