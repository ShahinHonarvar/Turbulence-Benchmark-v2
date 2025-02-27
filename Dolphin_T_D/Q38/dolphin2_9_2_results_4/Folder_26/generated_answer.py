def find_subset_of_length_n(elements):
    n = 25
    count = 0
    for i in range(len(elements) + 1):
        if len(elements) - i == n:
            for comb in combinations(elements, i):
                count += 1
    return count