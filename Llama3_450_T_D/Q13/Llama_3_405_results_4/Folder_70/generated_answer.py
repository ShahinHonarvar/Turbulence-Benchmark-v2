def find_second_largest_num(num_list):
    sliced_list = num_list[28:33]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]