def find_subsets_of_length_n(s):
    count = 0
    for subset in itertools.combinations(s, 86):
        count += 1
    return count