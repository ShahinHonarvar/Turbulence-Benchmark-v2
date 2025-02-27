def find_second_largest_num(num_list):
    if len(num_list) < 34 or len(num_list) > 37:
        return 'None'
    num_list = num_list[33:37]
    num_list.sort()
    if len(num_list) < 2:
        return 'None'
    return num_list[-2]