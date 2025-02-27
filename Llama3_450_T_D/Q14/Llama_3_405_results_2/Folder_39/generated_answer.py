def find_second_smallest_num(num_list):
    if len(num_list) < 29 or len(num_list) < 41:
        sliced_list = num_list[28:]
    else:
        sliced_list = num_list[28:41]
    if len(sliced_list) < 2:
        return None
    else:
        sliced_list.sort()
        return sliced_list[1]