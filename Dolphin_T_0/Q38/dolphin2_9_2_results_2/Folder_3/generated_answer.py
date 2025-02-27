def find_subset_of_length_n(elements):
    if len(elements) < 100:
        return 0
    n = len(elements)
    count = 0
    for i in range(1 << n):
        subset = [elements[j] for j in range(n) if i & 1 << j]
        if len(subset) == 100:
            count += 1
    return count