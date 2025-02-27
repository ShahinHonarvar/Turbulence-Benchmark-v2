def find_second_largest_num(num_list):
    sub_list = num_list[28:39]
    if len(sub_list) < 2:
        return None
    else:
        max_num = max(sub_list)
        sub_list.remove(max_num)
        return max(sub_list)