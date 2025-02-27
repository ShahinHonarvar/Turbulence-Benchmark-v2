def find_second_smallest_num(num_list):
    if len(num_list) < 7:
        return None
    num_list = num_list[:7]
    min_num = min(num_list)
    num_list.remove(min_num)
    if len(num_list) == 0:
        return None
    return min(num_list)