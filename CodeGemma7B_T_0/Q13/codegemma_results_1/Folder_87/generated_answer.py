def find_second_largest_num(num_list):
    if len(num_list) < 37 or len(num_list) > 47:
        return 'None'
    num_list = num_list[36:47]
    num_list.sort()
    return num_list[-2]