def find_second_smallest_num(num_list):
    if len(num_list) < 2:
        return None
    min_num = min(num_list)
    num_list.remove(min_num)
    return min(num_list)