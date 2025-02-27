def find_second_largest_num(num_list):
    sliced_list = num_list[3:6]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[-2]