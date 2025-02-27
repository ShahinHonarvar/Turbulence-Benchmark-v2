def all_ints_inclusive(int_list):
    start_index = 56
    end_index = 82
    if start_index < 0 or end_index >= len(int_list) or start_index > end_index:
        return []
    return int_list[start_index:end_index + 1]