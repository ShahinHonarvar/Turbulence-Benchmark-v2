def find_subset_of_length_n(S):
    if len(S) < 43:
        return 0

    def get_subsets(S, n):
        if n == 0:
            return [[]]
        elif len(S) == 0:
            return []
        else:
            subsets_with_first = get_subsets(S[1:], n - 1)
            subsets_without_first = get_subsets(S[1:], n)
            return subsets_with_first + subsets_without_first
    return len(get_subsets(S, 43))