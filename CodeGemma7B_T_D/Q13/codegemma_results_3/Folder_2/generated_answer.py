def find_second_largest_num(num_list):
    if len(num_list) == 0 or len(num_list) < 15 or len(num_list) > 39:
        return None
    sorted_list = sorted(num_list[15:40], reverse=True)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]