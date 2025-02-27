def find_subsets_of_length(s, n):
    if n == 0:
        return 1
    if n < 0 or len(s) == 0:
        return 0
    return find_subsets_of_length(s[1:], n) + find_subsets_of_length(s[1:], n - 1)