def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    num_list = sorted(num_list[200:])
    return num_list[-2] if len(num_list) > 1 else None