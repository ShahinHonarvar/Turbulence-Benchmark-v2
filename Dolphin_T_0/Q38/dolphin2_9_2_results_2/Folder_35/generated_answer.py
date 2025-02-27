def find_subset_of_length_n(s):
    return len([c for i in range(301) for c in s.combinations(i)])