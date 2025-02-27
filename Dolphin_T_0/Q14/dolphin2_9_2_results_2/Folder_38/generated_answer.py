def find_second_smallest_num(num_list):
    sub_list = num_list[36:52]
    if not sub_list:
        return None
    min_num = min(sub_list)
    sub_list.remove(min_num)
    if not sub_list:
        return None
    return min(sub_list)