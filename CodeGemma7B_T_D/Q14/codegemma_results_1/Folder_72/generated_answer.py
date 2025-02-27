def find_second_smallest_num(num_list):
    if not num_list:
        return None
    sliced_list = num_list[82:87]
    if not sliced_list:
        return None
    sorted_list = sorted(sliced_list)
    return sorted_list[1]