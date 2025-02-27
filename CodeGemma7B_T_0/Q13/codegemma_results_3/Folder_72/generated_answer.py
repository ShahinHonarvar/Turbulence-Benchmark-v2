def find_second_largest_num(num_list):
    if len(num_list) < 29 or len(num_list) > 51:
        return 'None'
    num_list = sorted(num_list[29:52])
    if len(num_list) < 2:
        return 'None'
    return num_list[-2]