def find_second_largest_num(num_list):
    num_list = num_list[55:99]
    if len(num_list) < 2:
        return None
    max_num = max(num_list)
    num_list.remove(max_num)
    if len(num_list) < 1:
        return None
    second_max = max(num_list)
    return second_max