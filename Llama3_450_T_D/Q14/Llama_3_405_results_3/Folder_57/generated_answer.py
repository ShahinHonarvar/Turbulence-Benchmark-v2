def find_second_smallest_num(num_list):
    if len(num_list) < 31:
        return None
    sliced_list = num_list[20:31]
    sliced_list.sort()
    if len(sliced_list) > 1:
        return sliced_list[1]
    else:
        return None