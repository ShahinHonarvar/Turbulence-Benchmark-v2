def find_second_largest_num(num_list):
    if len(num_list) < 10 or len(set(num_list)) != len(num_list):
        return None
    num_list = sorted(num_list[8:10])
    if len(num_list) < 2:
        return None
    return num_list[-2]