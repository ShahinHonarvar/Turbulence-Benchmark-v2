def find_subset_of_length_n(n):
    if len(n) < 27:
        return 0
    elif len(n) == 27:
        return 2 ** len(n)
    else:
        return 2 ** len(n) - 1