def find_subset_of_length_n(input_set):
    n = 92
    if len(input_set) < n:
        return 0
    count = 0

    def find_subset_recursively(start_index, current_subset):
        nonlocal count
        if len(current_subset) == n:
            count += 1
            return
        if start_index == len(input_set):
            return
        for i in range(start_index, len(input_set)):
            find_subset_recursively(i + 1, current_subset + [input_set[i]])
    find_subset_recursively(0, [])
    return count