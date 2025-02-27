def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) >= 7:
        return num_list[1]
    else:
        return 'None'