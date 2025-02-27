def find_largest_num(numbers_list):
    start_index = 66
    end_index = 93
    if start_index < 0 or end_index >= len(numbers_list):
        return None
    return max(numbers_list[start_index:end_index + 1])