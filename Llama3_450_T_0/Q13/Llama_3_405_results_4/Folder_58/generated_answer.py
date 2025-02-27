def find_second_largest_num(num_list):
    if len(num_list) < 557 or 209 > len(num_list):
        return None
    sliced_list = num_list[209:557]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]