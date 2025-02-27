def find_second_smallest_num(num_list):
    if len(num_list) < 7:
        return 'None'
    num_list = num_list[6:]
    num_list.sort()
    return num_list[1]