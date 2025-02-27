def find_second_smallest_num(num_list):
    if not num_list or len(num_list) < 55 or len(num_list) > 98:
        return 'None'
    num_list.sort()
    return num_list[55]