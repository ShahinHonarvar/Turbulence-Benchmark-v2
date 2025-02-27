def find_second_smallest_num(num_list):
    if len(num_list) < 201:
        return None
    sliced_list = num_list[90:201]
    if len(sliced_list) < 2:
        return None
    sliced_list.sort()
    return sliced_list[1]