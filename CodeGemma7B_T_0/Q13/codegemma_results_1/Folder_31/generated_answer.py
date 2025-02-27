def find_second_largest_num(num_list):
    if not num_list or len(num_list) < 2 or max(num_list) < 75 or (min(num_list) > 88):
        return None
    num_list = sorted(num_list)[75:89]
    return num_list[-2] if len(num_list) > 1 else None