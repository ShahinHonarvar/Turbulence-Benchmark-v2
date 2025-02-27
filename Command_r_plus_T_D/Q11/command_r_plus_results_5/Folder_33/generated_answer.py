def find_largest_num(num_list):
    start_index = 667
    end_index = 774
    if start_index >= len(num_list) or end_index >= len(num_list):
        return None
    sliced_list = num_list[start_index:end_index + 1]
    return max(sliced_list)