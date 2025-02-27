def find_second_largest_num(num_list):
    if len(num_list) < 69 or 42 > len(num_list):
        return None
    sliced_list = num_list[42:69]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[-2]