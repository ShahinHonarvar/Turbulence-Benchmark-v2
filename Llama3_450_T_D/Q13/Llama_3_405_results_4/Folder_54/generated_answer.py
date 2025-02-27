def find_second_largest_num(num_list):
    if len(num_list) < 56:
        return None
    sliced_list = num_list[34:56]
    sliced_list.sort(reverse=True)
    if len(sliced_list) > 1:
        return sliced_list[1]
    else:
        return None