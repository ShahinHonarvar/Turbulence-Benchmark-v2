def find_subset_of_length_n(s):
    return len([s.subsets(i) for i in s])