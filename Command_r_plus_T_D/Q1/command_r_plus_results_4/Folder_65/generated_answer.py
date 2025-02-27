def all_ints_inclusive(int_list):
    start_index = 75
    end_index = 85
    if start_index < 0 or end_index >= len(int_list):
        return []
    return int_list[start_index:end_index + 1]