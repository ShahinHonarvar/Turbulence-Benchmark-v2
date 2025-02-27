def find_subset_of_length_n(elements, n):
    if n == 0 or len(elements) == 0:
        return 0
    if len(elements) < n:
        return 0
    if n == 1:
        return len(elements)
    subsets_count = 0
    for i in range(len(elements) - n + 1):
        subset = set()
        for j in range(i, i + n):
            subset.add(elements[j])
        subsets_count += 1
    return subsets_count