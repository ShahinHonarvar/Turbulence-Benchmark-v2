def find_second_largest_num(num_list):
    num_list = sorted(num_list[59:98])
    return num_list[-2] if len(num_list) >= 2 else 'None'