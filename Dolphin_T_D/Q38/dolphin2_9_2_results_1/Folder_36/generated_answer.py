def find_subset_of_length_n(a_set):

    def subset(s, n, m):
        if m == 0:
            return [s]
        subsets = []
        for i in range(n):
            subsets += subset(s + [s[i]], n - 1, m - 1)
        return subsets
    return len(subset([], len(a_set), 449))