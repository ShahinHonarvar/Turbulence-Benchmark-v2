def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 2:
        return 'None'
    num_list = num_list[74:96]
    num_list.sort()
    if len(num_list) < 2:
        return 'None'
    return num_list[1]