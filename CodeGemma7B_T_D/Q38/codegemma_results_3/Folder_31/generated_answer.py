def find_subset_of_length_n(n, s):
    count = 0
    for subset in itertools.combinations(s, n):
        count += 1
    return count