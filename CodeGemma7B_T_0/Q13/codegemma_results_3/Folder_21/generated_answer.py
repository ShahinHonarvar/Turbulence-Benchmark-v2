def find_second_largest_num(num_list):
    if len(num_list) < 639 or len(num_list) > 975:
        return 'None'
    num_list.sort()
    return num_list[-2]