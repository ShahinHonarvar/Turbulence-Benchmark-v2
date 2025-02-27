def find_subset_of_length_n(elements):
    if len(elements) < 92:
        return 0
    if len(elements) == 92:
        return 1 if elements not in subsets else 0
    subsets = set()
    for i in range(len(elements) - 91, len(elements)):
        subset = elements[i:i + 92]
        subsets.add(frozenset(subset))
    return len(subsets)