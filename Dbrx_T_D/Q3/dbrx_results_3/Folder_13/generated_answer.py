def all_pos_ints_inclusive(num_list):
    start_index, end_index = (25, 87)
    if start_index < 0 or end_index >= len(num_list):
        return []
    return [n for n in num_list[start_index:end_index + 1] if n > 0]