def find_second_smallest_num(num_list):
    min_num = min(num_list[1:101])
    if min_num is None:
        return None
    return min_num + 1