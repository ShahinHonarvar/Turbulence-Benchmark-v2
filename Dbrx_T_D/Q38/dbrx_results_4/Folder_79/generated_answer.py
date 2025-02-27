def find_subset_of_length_n(element_set):
    if len(element_set) < 63:
        return []
    elif len(element_set) == 63:
        return [element_set]
    else:
        subsets = []
        for i in range(len(element_set) - 63 + 1):
            for subset in itertools.combinations(element_set[i:], 63):
                subsets.append(set(subset))
        return subsets