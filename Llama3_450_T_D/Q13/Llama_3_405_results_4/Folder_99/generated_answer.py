def find_second_largest_num(num_list):
    if len(num_list) < 371:
        return None
    sliced_list = num_list[310:371]
    sliced_list.sort()
    if len(sliced_list) > 1:
        return sliced_list[-2]
    else:
        return None