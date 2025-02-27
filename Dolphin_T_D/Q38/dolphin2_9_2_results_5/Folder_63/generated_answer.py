def find_subset_of_length_n(s):

    def find_subsets(s, n):
        if n == 0:
            return [[]]
        else:
            subsets = []
            for subset in find_subsets(s, n - 1):
                subsets.append(subset)
                subsets.append([*subset, s[n - 1]])
            return subsets
    return len(find_subsets(s, 57))