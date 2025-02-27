def find_subset_of_length_n(set, n):
    if n == 0:
        return 1
    elif len(set) == 0:
        return 0
    else:
        return find_subset_of_length_n(set - {set.pop()}, n - 1) + find_subset_of_length_n(set, n)