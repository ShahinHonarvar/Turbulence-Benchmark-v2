def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 29 or len(num_list) > 51:
        return 'None'
    num_list = sorted(num_list[29:52])
    return num_list[1]