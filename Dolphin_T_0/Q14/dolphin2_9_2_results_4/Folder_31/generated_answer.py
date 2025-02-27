def find_second_smallest_num(num_list):
    if not num_list:
        return None
    sl_list = num_list[29:94]
    if len(sl_list) < 2:
        return None
    smallest = min(sl_list)
    sl_list.remove(smallest)
    second_smallest = min(sl_list)
    return second_smallest