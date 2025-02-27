def find_subset_of_length_n(elements):
    if len(elements) < 307:
        return []
    subsets = []
    for i in range(len(elements) - 307 + 1):
        subsets.append(elements[i:i + 307])
    return subsets