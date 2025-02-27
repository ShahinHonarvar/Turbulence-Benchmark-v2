def find_second_largest_num(num_list):
    sub_list = num_list[667:775]
    if len(sub_list) < 2:
        return None
    else:
        sorted_sub_list = sorted(sub_list)
        return sorted_sub_list[-2]