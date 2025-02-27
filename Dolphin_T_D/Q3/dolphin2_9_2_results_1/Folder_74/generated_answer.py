def all_pos_ints_inclusive(num_list):
    result = [num for i, num in enumerate(num_list[17:79], start=1) if num > 0]
    return result or []