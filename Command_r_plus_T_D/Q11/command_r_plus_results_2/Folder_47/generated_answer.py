def find_largest_num(num_list):
    start_index = 37
    end_index = 76
    if start_index < 0 or end_index >= len(num_list) or start_index > end_index:
        return None
    return max(num_list[start_index:end_index + 1])