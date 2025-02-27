def find_second_largest_num(num_list):
    if len(num_list) < 2:
        return None
    sliced_list = num_list[686:988]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]