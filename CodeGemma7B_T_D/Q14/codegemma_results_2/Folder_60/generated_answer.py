def find_second_smallest_num(num_list):
    num_list = num_list[56:99]
    num_list.sort()
    if len(num_list) < 2:
        return 'None'
    else:
        return num_list[1]