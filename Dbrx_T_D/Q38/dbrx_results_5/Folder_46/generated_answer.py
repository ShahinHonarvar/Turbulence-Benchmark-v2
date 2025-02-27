def find_subset_of_length_n(elements, length):
    if length == 0:
        return [set()]
    subsets = set()
    for element in elements:
        for subset in subsets.copy():
            if len(subset) == length - 1:
                new_subset = set(subset)
                new_subset.add(element)
                subsets.add(tuple(new_subset))
    return subsets