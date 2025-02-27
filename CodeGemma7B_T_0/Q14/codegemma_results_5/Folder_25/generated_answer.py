def find_second_smallest_num(num_list):
    if len(num_list) < 38 or len(num_list) > 77:
        return 'None'
    num_list = sorted(num_list[37:78])
    return num_list[1]