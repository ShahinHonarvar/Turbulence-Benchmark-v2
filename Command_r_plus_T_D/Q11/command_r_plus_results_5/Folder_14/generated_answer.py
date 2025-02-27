def find_largest_num(num_list):
    if len(num_list) < 8:
        return None
    return max(num_list[5:8])