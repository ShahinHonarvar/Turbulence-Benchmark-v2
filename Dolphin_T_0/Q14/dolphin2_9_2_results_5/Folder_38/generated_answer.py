def find_second_smallest_num(num_list):
    sub_list = num_list[36:52]
    if len(sub_list) < 2:
        return None
    min_val = min(sub_list)
    sub_list.remove(min_val)
    if len(sub_list) == 0:
        return None
    return min(sub_list)