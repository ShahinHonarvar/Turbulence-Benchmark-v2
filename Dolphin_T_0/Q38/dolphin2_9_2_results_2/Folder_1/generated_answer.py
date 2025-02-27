def find_subset_of_length_n(s):
    return len([c for c in s.powerset() if len(c) == 85])