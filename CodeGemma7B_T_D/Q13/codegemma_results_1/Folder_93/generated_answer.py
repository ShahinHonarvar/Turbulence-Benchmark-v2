def find_second_largest_num(num_list):
    if len(num_list) < 75 or len(num_list) > 95:
        return None
    num_list = sorted(num_list[75:95 + 1])
    return num_list[-2] if len(num_list) > 1 else None