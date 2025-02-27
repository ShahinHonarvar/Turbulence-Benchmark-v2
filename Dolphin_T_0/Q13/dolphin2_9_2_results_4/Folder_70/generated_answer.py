def find_second_largest_num(input_list):
    sub_list = input_list[28:33]
    if len(sub_list) < 2:
        return None
    max_num = max(sub_list)
    sub_list.remove(max_num)
    if len(sub_list) < 2:
        return None
    second_max_num = max(sub_list)
    return second_max_num