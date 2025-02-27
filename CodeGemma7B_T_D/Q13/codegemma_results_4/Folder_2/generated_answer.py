def find_second_largest_num(num_list):
    num_list.sort()
    if len(num_list) == 0 or len(num_list) <= 15 or len(num_list) >= 39:
        return 'None'
    else:
        return num_list[-2]