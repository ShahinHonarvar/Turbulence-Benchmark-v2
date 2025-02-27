def find_subset_of_length_n(n, s):
    if n == 0:
        return 1
    elif len(s) == 0:
        return 0
    else:
        return find_subset_of_length_n(n - 1, s[1:]) + find_subset_of_length_n(n, s[:-1])