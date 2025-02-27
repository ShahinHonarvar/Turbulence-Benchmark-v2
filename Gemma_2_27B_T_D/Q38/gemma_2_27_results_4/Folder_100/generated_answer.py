def find_subset_of_length_n(elements):
    n = 99
    total_subsets = 2 ** len(elements)
    count = 0
    for i in range(total_subsets):
        subset = {element for j, element in enumerate(elements) if i >> j & 1}
        if len(subset) == n:
            count += 1
    return count