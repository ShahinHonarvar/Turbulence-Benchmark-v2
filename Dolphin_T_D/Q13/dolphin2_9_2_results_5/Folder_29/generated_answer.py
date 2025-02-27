def find_second_largest_num(num_list):
    tmp = num_list[59:98]
    if len(tmp) < 2:
        return None
    max_num = max(tmp)
    tmp.remove(max_num)
    if len(tmp) < 2:
        return None
    second_max_num = max(tmp)
    return second_max_num