def find_second_largest_num(input_list):
    if len(input_list) < 52:
        return None
    sub_list = input_list[37:52]
    if len(set(sub_list)) < 2:
        return None
    sub_list.sort(reverse=True)
    return sub_list[1]