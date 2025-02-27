def find_second_smallest_num(num_list):
    if len(num_list) < 82 or len(num_list) > 86:
        return 'None'
    num_list = num_list[82:87]
    num_list.sort()
    return num_list[1]