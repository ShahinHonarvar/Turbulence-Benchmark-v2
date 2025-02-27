def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    min_num = min(num_list[0:8])
    num_list.remove(min_num)
    if len(num_list) < 2:
        return None
    return min(num_list[0:8])