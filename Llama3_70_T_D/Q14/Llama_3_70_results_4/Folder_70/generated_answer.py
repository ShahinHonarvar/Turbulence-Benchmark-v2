def find_second_smallest_num(num_list):
    if 50 > len(num_list) or 35 >= len(num_list):
        return None
    target_list = sorted(num_list[35:50])
    if len(target_list) < 2:
        return None
    return target_list[1]