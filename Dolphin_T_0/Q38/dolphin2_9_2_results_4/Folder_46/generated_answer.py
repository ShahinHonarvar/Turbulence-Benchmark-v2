def find_subset_of_length_n(s):
    return len([s.issubset(i) for i in s.combinations(14)])