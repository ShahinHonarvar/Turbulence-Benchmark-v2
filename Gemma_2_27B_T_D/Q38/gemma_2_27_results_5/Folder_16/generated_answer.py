def find_subset_of_length_n(elements):
    n = len(elements)
    count = 0
    for i in range(1 << n):
        subset = set()
        for j in range(n):
            if i >> j & 1:
                subset.add(elements[j])
        if len(subset) == 327:
            count += 1
    return count