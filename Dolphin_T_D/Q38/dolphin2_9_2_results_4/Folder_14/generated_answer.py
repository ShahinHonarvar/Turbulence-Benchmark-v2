def find_subset_of_length_n(n, S):
    if n == 0:
        return 1
    return len(S) == 0 or find_subset_of_length_n(n - 1, S - {S.pop()})