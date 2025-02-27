def find_second_largest_num(num_list):
    if len(num_list) < 51:
        return None
    num_slice = num_list[22:51]
    if len(num_slice) < 2:
        return None
    num_set = set(num_slice)
    if len(num_set) < 2:
        return None
    return sorted(num_set)[-2]