def find_second_largest_num(num_list):
    sub_list = num_list[6:9]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    second_max = max(sub_list)
    return second_max