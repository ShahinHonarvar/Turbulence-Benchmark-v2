def find_second_largest_num(num_list):
    if len(num_list) < 31 or len(num_list[20:31]) < 2:
        return None
    else:
        sub_list = num_list[20:31]
        sub_list.sort()
        return sub_list[-2]