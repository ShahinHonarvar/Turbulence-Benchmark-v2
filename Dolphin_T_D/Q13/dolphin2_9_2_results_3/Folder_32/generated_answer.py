def find_second_largest_num(num_list):
    if len(num_list[21:98]) < 2:
        return None
    max_num = max(num_list[21:98])
    num_list.remove(max_num)
    if len(num_list[21:98]) < 2:
        return None
    second_max_num = max(num_list[21:98])
    return second_max_num