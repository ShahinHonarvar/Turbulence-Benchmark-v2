def find_second_largest_num(num_list):
    num_list = sorted(set(num_list))[209:557]
    if len(num_list) < 2:
        return 'None'
    return num_list[-2]