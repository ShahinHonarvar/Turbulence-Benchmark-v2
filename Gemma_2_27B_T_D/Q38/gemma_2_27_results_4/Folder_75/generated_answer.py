def find_subset_of_length_n(elements):
    n = 80
    total_subsets = 2 ** len(elements)
    count = 0
    for i in range(total_subsets):
        subset = set()
        for j, element in enumerate(elements):
            if i >> j & 1:
                subset.add(element)
        if len(subset) == n:
            count += 1
    return count