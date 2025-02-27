def find_subset_of_length_n(input_set):
    n = 0
    count = 0
    for i in range(2 ** len(input_set)):
        subset = [input_set[j] for j in range(len(input_set)) if i & 1 << j]
        if len(subset) == n:
            count += 1
    return count