def find_second_smallest_num(num_list):
    if len(num_list) < 201 or 90 > len(num_list):
        return None
    sliced_list = num_list[90:201]
    sliced_list.sort()
    if len(sliced_list) < 2:
        return None
    return sliced_list[1]