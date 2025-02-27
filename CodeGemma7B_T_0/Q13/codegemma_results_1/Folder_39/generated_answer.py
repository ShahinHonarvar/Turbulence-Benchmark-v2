def find_second_largest_num(num_list):
    if len(num_list) < 21 or len(num_list) > 31:
        return 'None'
    num_list = sorted(num_list[20:31])
    if len(num_list) < 2:
        return 'None'
    return num_list[-2]