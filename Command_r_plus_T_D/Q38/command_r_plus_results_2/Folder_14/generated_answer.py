def find_subset_of_length_n(elements_set):
    n = len(elements_set)
    total_subsets = 0
    if n >= 17:
        total_subsets = binomial_coefficient(n, 17)
    return total_subsets

def binomial_coefficient(n, k):
    if k > n:
        return 0
    if k == 0 or k == n:
        return 1
    return binomial_coefficient(n - 1, k - 1) + binomial_coefficient(n - 1, k)