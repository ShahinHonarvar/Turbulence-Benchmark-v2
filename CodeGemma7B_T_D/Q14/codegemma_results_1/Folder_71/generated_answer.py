def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return 'None'
    if 29 > len(num_list) or 51 >= len(num_list):
        return 'None'
    num_list = sorted(num_list[29:52])
    return num_list[1]