def find_second_largest_num(num_list):
    if len(num_list) < 50:
        return None
    sliced_list = num_list[35:50]
    sliced_list.sort(reverse=True)
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]