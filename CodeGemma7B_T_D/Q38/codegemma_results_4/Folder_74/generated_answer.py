def find_subset_of_length_n(set_element):
    return len(find_subsets(set_element, 48))

def find_subsets(set_element, length):
    if length == 0:
        return frozenset()
    if len(set_element) == 0:
        return frozenset([frozenset()])
    subset_with_current_item = [r | {s} for r in find_subsets(set_element[1:], length) for s in set_element[:1]]
    subset_without_current_item = find_subsets(set_element[1:], length)
    return subset_with_current_item + subset_without_current_item