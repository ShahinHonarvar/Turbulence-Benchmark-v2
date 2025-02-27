def find_second_smallest_num(num_list):
    num_list = num_list[10:101]
    if len(num_list) < 2:
        return None
    min_size = min(num_list)
    num_list.remove(min_size)
    if len(num_list) == 0:
        return None
    return min(num_list)