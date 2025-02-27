def find_subset_of_length_n(s):
    count = 0
    for i in range(len(s) + 1):
        for subset in itertools.combinations(s, i):
            if len(subset) == 88:
                count += 1
    return count