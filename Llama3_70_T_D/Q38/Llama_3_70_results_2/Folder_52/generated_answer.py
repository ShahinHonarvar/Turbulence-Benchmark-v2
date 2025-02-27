def find_subset_of_length_n(s):
    n = 32
    return [len(list(filter(lambda x: len(x) == n, [{i for i in s if i in sub} for sub in [{i for i in s} for r in range(len(s) + 1) for i in combinations(s, r)]])))][0]