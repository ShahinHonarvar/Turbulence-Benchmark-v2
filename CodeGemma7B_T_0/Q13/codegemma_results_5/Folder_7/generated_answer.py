def find_second_largest_num(num_list):
    num_list = num_list[661:925]
    num_list.sort()
    if len(num_list) < 2:
        return 'None'
    return num_list[-2]