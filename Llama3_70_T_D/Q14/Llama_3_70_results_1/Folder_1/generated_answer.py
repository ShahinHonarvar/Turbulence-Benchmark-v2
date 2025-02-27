def find_second_smallest_num(num_list):
    if 34 >= len(num_list) or 55 >= len(num_list):
        return None
    sub_list = num_list[34:56]
    sub_list.sort()
    if len(sub_list) == 1:
        return None
    return sub_list[1]