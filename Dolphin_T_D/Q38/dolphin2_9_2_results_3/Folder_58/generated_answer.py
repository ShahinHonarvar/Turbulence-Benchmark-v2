def find_subset_of_length_n(s):
    size = 0

    def find_combinations(currentSet, i, size):
        nonlocal max_size
        if i <= 0 or size > max_size:
            return
        find_combinations(currentSet - set([i]), i - 1, size)
        find_combinations(set(currentSet), i - 1, size + 1)
    find_combinations(s, len(s), 0)
    return size