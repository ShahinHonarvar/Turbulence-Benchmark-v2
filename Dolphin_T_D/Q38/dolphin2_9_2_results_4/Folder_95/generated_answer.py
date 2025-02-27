def find_subset_of_length_n(s):

    def num_subsets(s, n):
        if n == 0:
            return 1
        if not s or n < 0:
            return 0
        return num_subsets(s[1:], n - 1) + num_subsets(s[1:], n)
    return num_subsets(s, 87)