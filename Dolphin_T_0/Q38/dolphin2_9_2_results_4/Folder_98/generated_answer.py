def find_subset_of_length_n(set_elements):
    return len([subset for subset in _generate_subsets(set_elements) if len(subset) == 4])

def _generate_subsets(set_elements):
    if len(set_elements) == 0:
        return [[]]
    subsets = _generate_subsets(set_elements[1:])
    return subsets + [[set_elements[0]] + subset for subset in subsets]