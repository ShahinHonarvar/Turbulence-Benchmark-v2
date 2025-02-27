def find_second_largest_num(num_list):
    num_list = sorted(num_list)
    if len(num_list) <= 66 or len(num_list) <= 93:
        return None
    return num_list[-2]