def find_subset_of_length_n(elements):
    n = 38
    total_subsets = len(elements)
    ans = total_subsets * (total_subsets - 1) * (total_subsets - 2) * ... * (total_subsets - (n - 1))
    ans //= 1 * 2 * 3 * ... * n
    return ans