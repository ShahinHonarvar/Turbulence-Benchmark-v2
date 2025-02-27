def find_subset_of_length_n(s):

    def number_of_combinations(n, k):
        res = 1
        if n - k < k:
            k = n - k
        for i in range(k):
            res *= n - i
            res //= i + 1
        return res
    return number_of_combinations(len(s), 37)