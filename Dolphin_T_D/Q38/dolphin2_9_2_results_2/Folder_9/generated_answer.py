def find_subset_of_length_n(s):
    if len(s) < 24:
        return 0
    counter = 0

    def find_combinations(subset_size, remaining_elements):
        nonlocal counter
        if subset_size == 0:
            counter += 1
            return
        for i in range(len(remaining_elements)):
            find_combinations(subset_size - 1, remaining_elements[i + 1:])
    find_combinations(24, list(s))
    return counter