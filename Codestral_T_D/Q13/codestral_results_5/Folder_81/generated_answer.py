def find_second_largest_num(num_list):
    sub_list = num_list[10:101]
    sub_list.sort()
    if len(sub_list) >= 2:
        return sub_list[-2]
    else:
        return None