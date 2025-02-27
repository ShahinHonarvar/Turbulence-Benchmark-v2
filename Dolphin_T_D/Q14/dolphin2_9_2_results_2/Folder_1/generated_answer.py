def find_second_smallest_num(num_list):
    if len(num_list) < 2 or len(num_list) < 34 or 55 < len(num_list):
        return None
    min1 = min(num_list[33:56])
    num_list.remove(min1)
    if len(num_list) < 2:
        return None
    min2 = min(num_list)
    return min2