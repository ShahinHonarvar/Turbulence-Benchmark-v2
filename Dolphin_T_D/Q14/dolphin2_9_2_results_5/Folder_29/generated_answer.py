def find_second_smallest_num(num_list):
    if 98 < len(num_list) < 55:
        return None
    sub_list = num_list[54:99]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]