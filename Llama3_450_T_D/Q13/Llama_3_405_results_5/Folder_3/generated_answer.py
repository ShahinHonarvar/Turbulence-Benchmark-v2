def find_second_largest_num(num_list):
    sliced_list = num_list[62:93]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[-2]