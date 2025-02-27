def find_second_largest_num(num_list):
    if len(num_list) < 28 or len(num_list) > 56:
        return None
    num_list = sorted(num_list[27:56])
    if len(num_list) < 2:
        return None
    return num_list[-2]