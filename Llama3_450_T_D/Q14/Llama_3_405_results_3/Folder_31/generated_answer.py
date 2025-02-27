def find_second_smallest_num(num_list):
    if len(num_list) < 2 or 93 >= len(num_list) or 29 < 0:
        return None
    sliced_list = num_list[29:94]
    sorted_list = sorted(sliced_list)
    if len(sorted_list) < 2:
        return None
    return sorted_list[1]