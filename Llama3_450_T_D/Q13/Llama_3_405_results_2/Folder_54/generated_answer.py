def find_second_largest_num(num_list):
    if len(num_list) < 56:
        sliced_list = num_list[34:]
    else:
        sliced_list = num_list[34:56]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    else:
        return sliced_list[1]