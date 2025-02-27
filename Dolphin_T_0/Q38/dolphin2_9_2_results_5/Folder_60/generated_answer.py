def find_subset_of_length_n(s):

    def num_combinations(n, r):
        if r == 0 or n == r:
            return 1
        return num_combinations(n - 1, r - 1) + num_combinations(n - 1, r)
    return num_combinations(len(s), 88)