def find_second_smallest_num(num_list):
    if len(num_list) < 21 or len(num_list) > 31:
        return 'None'
    num_list = num_list[20:31]
    num_list.sort()
    return num_list[1]