def find_subset_of_length_n(data):
    n = 60
    count = 0
    for i in range(len(data) + 1):
        for subset in itertools.combinations(data, i):
            if len(subset) == n:
                count += 1
    return count