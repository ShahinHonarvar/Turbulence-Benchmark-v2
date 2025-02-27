def find_second_largest_num(input_list):
    if 78 < len(input_list) < 62:
        return None
    sub_list = input_list[62:79]
    if len(set(sub_list)) < 2:
        return None
    else:
        sorted_sub_list = sorted(set(sub_list), reverse=True)
        return sorted_sub_list[1]