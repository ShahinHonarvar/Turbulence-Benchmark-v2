def find_second_smallest_num(num_list):
    sliced_list = num_list[22:51]
    if len(sliced_list) < 2:
        return None
    return sorted(sliced_list)[1]