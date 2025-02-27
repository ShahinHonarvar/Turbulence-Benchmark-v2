def find_second_largest_num(num_list):
    if len(num_list) < 10 or len(num_list) > 66:
        return None
    num_list = sorted(num_list)
    return num_list[-2] if len(num_list) > 10 else None