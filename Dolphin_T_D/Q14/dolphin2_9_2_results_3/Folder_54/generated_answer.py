def find_second_smallest_num(num_list):
    sub_list = num_list[68:87]
    if len(sub_list) < 2:
        return None
    min_num = min(sub_list)
    sub_list.remove(min_num)
    return min(sub_list) if len(sub_list) > 0 else None