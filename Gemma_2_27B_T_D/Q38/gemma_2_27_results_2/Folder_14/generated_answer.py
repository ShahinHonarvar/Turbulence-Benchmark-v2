def find_subset_of_length_n(elements):
    total_subsets = 2 ** len(elements)
    subsets_of_length_17 = total_subsets - (binom(len(elements), 0) + binom(len(elements), 1) + ... + binom(len(elements), 16) + binom(len(elements), len(elements)))
    return subsets_of_length_17

def binom(n, k):
    if k < 0 or k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binom(n - 1, k - 1) + binom(n - 1, k)