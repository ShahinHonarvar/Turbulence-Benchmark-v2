def find_second_smallest_num(num_list):
    if len(num_list) > 88:
        sub_list = num_list[75:89]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[1]
    return None