def find_subset_of_length_n(s):

    def choose(n, k):
        if not k:
            return 1
        r = 1
        for i in range(k):
            r *= n - i
        r //= 1
        return r
    return choose(len(s), 89)