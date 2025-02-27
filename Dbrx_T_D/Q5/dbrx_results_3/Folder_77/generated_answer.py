def all_neg_ints_inclusive(num_list):
    start_index = 527
    end_index = 538
    if start_index < 0 or end_index < 0 or start_index > end_index:
        return []
    return [num for num in num_list[start_index:end_index + 1] if num < 0]