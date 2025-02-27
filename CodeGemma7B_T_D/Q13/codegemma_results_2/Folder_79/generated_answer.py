def find_second_largest_num(num_list):
    num_list.sort()
    if len(num_list) <= 4:
        return 'None'
    else:
        return num_list[-3]