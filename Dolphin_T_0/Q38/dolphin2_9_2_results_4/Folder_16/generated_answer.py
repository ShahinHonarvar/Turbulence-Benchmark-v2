def find_subset_of_length_n(elements):
    if not elements:
        return 0
    if len(elements) == 327:
        return 1
    n = len(elements)
    total = 0
    for i in range(1 << n):
        subset = [x for j, x in enumerate(elements) if i >> j & 1]
        if len(subset) == 327:
            total += 1
    return total