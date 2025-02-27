def find_subset_of_length_n(s):
    n = 94
    if n > len(s):
        return 0
    elif n == len(s):
        return 1
    else:
        subsets = [combo for combo in itertools.combinations(s, n)]
        return len(subsets)