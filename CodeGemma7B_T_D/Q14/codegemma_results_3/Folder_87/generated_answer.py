def find_second_smallest_num(num_list):
    num_list = sorted(num_list[22:89])
    if len(num_list) < 2:
        return 'None'
    else:
        return num_list[1]