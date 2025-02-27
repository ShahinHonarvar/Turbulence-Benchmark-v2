def find_second_largest_num(num_list):
    if len(num_list) < 100:
        return None
    sliced_list = sorted(num_list[62:100])
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]