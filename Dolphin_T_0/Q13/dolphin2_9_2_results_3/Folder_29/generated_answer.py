def find_second_largest_num(num_list):
    filter_list = num_list[59:98]
    if len(filter_list) < 2:
        return None
    max_num = max(filter_list)
    filter_list.remove(max_num)
    if len(filter_list) < 1:
        return None
    second_max_num = max(filter_list)
    return second_max_num