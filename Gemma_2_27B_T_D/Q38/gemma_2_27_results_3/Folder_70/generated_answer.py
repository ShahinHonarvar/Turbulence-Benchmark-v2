def find_subset_of_length_n(elements):
    n = 534
    combinations = 1
    for i in range(n):
        combinations *= (len(elements) - i) / (i + 1)
    return int(combinations)