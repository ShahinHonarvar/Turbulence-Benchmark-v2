def find_second_largest_num(num_list):
    if not num_list:
        return None
    num_list = num_list[75:86]
    if len(num_list) < 2:
        return None
    max_num = max(num_list)
    num_list.remove(max_num)
    if len(num_list) == 0:
        return None
    return max(num_list)