def find_second_largest_num(num_list):
    num_list[:62] = []
    num_list[78:] = []
    num_list.sort()
    if len(num_list) > 1:
        return num_list[-2]
    else:
        return 'None'