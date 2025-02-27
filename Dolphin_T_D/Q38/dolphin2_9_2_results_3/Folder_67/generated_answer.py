def find_subset_of_length_n(s):

    def count_subsets(s, n):
        if n == 0:
            return 1
        if len(s) == 0 or len(s) < n:
            return 0
        return count_subsets(s - {s[0]}, n - 1) + count_subsets(s - {s[0]}, n)
    return count_subsets(s, 43)