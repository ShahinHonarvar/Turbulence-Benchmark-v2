def find_second_largest_num(num_list):
    if len(num_list) < 37 or len(num_list) > 51:
        return 'None'
    num_list.sort()
    return num_list[-2]