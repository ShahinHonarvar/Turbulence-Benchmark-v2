def find_subset_of_length_n(element_set):
    if len(element_set) < 67:
        return {}
    subsets = []
    for i in range(67):
        for j in range(len(element_set) - 67 + i + 1):
            subset = frozenset(element_set[j:j + 67 - i])
            if len(subset) == 67:
                subsets.append(subset)
    return len(set(subsets))