def find_subset_of_length_n(a):
    return 256 if len(a) == 78 else len(a) * find_subset_of_length_n(a[1:]) + find_subset_of_length_n(a[:-1])