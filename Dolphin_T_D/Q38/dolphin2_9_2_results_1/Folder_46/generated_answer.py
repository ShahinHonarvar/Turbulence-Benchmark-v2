def find_subset_of_length_n(s):

    def subset(s, n):
        if n == 0:
            return 1
        if len(s) == 0 or n < 0:
            return 0
        return subset(s[1:], n - 1) + subset(s[1:], n)
    return subset(s, 14)