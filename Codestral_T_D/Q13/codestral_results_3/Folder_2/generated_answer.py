def find_second_largest_num(num_list):
    sliced_list = num_list[15:40]
    sliced_list.sort()
    if len(sliced_list) >= 2:
        return sliced_list[-2]
    else:
        return None