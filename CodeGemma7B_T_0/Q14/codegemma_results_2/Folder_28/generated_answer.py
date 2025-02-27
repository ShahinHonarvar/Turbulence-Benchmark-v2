def find_second_smallest_num(num_list):
    if len(num_list) < 22 or len(num_list) > 50:
        return 'None'
    num_list.sort()
    return num_list[22]