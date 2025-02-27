def find_second_largest_num(num_list):
    num_list = sorted(num_list)
    if len(num_list) > 51:
        return num_list[len(num_list) - 2]
    else:
        return 'None'