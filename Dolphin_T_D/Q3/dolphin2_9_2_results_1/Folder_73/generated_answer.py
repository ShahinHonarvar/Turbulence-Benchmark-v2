def all_pos_ints_inclusive(lower_bound, upper_bound):
    return [num for num in range(lower_bound, upper_bound + 1) if num > 0]