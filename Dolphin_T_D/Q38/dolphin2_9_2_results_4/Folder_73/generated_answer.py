def find_subset_of_length_n(s):

    def find_combination(s, n):
        if n == 0:
            return 1
        else:
            return sum((find_combination(s - i, n - 1) for i in s if i > 0))
    return find_combination(len(s), 41)