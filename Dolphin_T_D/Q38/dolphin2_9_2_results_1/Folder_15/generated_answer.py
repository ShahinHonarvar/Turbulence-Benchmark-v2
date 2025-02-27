def find_subset_of_length_n(s):

    def find_combinations(i, j):
        if j == 0:
            return 1
        if i == 0:
            return 0
        return find_combinations(i - 1, j) + find_combinations(i - 1, j - 1)
    return find_combinations(len(s), 10)