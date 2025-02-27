def find_subset_of_length_n(s):
    return len([subset for subset in _generate_all_subsets(s) if len(subset) == 84])

def _generate_all_subsets(s):
    if not s:
        return [[]]
    else:
        head, *tail = s
        subsets = _generate_all_subsets(tail)
        return subsets + [subset + [head] for subset in subsets]