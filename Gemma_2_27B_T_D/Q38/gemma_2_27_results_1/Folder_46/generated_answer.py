def find_subset_of_length_n(s):
    n = len(s)
    return len([1 for i in range(1 << n) if sum([1 for j in range(n) if i >> j & 1]) == 14])