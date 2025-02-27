def find_second_largest_num(num_list):
    if len(num_list) < 89:
        return None
    sliced_list = num_list[75:89]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]