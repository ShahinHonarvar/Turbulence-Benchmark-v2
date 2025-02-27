def find_subset_of_length_n(input_set):
    n = 84
    count = 0
    for i in range(len(input_set) + 1):
        for subset in itertools.combinations(input_set, i):
            if len(subset) == n:
                count += 1
    return count