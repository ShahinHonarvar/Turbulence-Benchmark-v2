def find_subset_of_length_n(s):

    def find_combinations(s, n):
        if n == 0:
            return [[]]
        if n < 0 or not s:
            return []
        return [x + [v] for x in find_combinations(s - {v}, n - 1) for v in s]
    return len(find_combinations(s, 30))