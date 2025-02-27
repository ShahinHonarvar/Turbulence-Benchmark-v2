def find_subset_of_length_n(elements_set):
    if not isinstance(elements_set, set) or len(elements_set) < 307:
        return 0
    subsets = []
    for _ in range(len(elements_set) - 307 + 1):
        subset = set()
        for _ in range(307):
            element = elements_set.pop()
            subset.add(element)
        subsets.append(subset)
    return len(subsets)