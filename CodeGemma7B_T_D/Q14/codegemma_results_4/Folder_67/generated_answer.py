def find_second_smallest_num(num_list):
    if len(num_list) > 50 and len(num_list) > 54:
        num_list.sort()
        return num_list[51]
    else:
        return 'None'