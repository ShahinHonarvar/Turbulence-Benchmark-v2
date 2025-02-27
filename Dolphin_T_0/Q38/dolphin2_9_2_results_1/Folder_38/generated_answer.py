def find_subset_of_length_n(input_set):
    input_list = list(input_set)
    subset_size = 38
    subset_count = 0
    for i in range(len(input_list) + 1):
        for j in range(i + 1, len(input_list) + 1):
            if j - i == subset_size:
                subset_count += 1
    return subset_count