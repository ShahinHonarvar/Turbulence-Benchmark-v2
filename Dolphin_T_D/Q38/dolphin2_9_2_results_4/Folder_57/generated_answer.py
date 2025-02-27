def find_subset_of_length_n(elements):

    def count_subsets(s, n):
        if n == 0 or not s:
            return 1
        if n > len(s):
            return 0
        return count_subsets(s - s.pop(), n - 1) + count_subsets(s.pop(), n)
    return count_subsets(frozenset(elements), 92)