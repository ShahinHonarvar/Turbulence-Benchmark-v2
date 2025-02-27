def find_largest_num(num_list):
    if len(num_list) < 2:
        return None
    return max(num_list[0], num_list[1])