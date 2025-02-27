def find_subset_of_length_n(elements):
    n = 86
    count = 0
    for i in range(len(elements) + 1):
        for subset in itertools.combinations(elements, i):
            if len(subset) == n:
                count += 1
    return count