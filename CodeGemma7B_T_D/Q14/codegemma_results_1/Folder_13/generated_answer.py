def find_second_smallest_num(num_list):
    if len(num_list) < 30 or len(num_list) > 33:
        return 'None'
    num_list.sort()
    return num_list[28:33][1]