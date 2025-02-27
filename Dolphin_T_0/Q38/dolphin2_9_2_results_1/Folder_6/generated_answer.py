def find_subset_of_length_n(s):

    def helper(n, e):
        if n == 0:
            return 1
        elif n < 0 or not e:
            return 0
        else:
            return helper(n - 1, e - 1) + helper(n, e - 1)
    return helper(89, len(s))