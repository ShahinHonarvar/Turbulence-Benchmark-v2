def find_subset_of_length_n(s):

    def find_combinations(s, n):
        if n == 0:
            return [[]]
        elif not s:
            return []
        else:
            subsets = list()
            for subset in find_combinations(s[1:], n - 1):
                subsets.append([s[0]] + subset)
            subsets.extend(find_combinations(s[1:], n))
            return subsets
    return len(find_combinations(s, 49))