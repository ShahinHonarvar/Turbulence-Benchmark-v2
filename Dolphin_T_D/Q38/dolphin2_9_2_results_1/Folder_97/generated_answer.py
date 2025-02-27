def find_subset_of_length_n(s):

    def find_combinations(s, n):
        if n == 0:
            return [[]]
        if n < 0 or len(s) == 0:
            return []
        return [[s[0]] + c for c in find_combinations(s[1:], n - 1)] + find_combinations(s[1:], n)
    return len(find_combinations(s, 219))