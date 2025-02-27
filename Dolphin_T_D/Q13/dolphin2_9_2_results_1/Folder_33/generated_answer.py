def find_second_largest_num(input_list):
    sub_list = input_list[667:775]
    if len(sub_list) < 2:
        return None
    sorted_sub_list = sorted(set(sub_list), reverse=True)
    if len(sorted_sub_list) < 2:
        return None
    return sorted_sub_list[1]