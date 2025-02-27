def find_subset_of_length_n(elements):
    result = 0
    n = 66
    for i in range(len(elements) + 1):
        for subset in combinations(elements, i):
            if len(subset) == n:
                result += 1
    return result