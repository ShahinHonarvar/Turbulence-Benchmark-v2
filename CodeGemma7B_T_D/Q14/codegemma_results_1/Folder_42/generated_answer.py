def find_second_smallest_num(num_list):
    num_list.sort()
    if len(num_list) < 22 or len(num_list) > 97:
        return 'None'
    return num_list[21]