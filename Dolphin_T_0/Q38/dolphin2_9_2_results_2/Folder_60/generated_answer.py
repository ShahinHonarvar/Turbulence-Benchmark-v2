def find_subset_of_length_n(s):

    def helper(s, n):
        if n == 0:
            return 1
        elif len(s) == 0:
            return 0
        else:
            return helper(s[1:], n - 1) + helper(s[1:], n)
    return helper(s, 88)