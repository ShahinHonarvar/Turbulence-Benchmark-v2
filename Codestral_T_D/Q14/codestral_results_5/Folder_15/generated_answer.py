def find_second_smallest_num(num_list):
    if len(num_list) <= 3:
        num_list.sort()
        if len(num_list) > 1:
            return num_list[1]
    else:
        sub_list = num_list[0:4]
        sub_list.sort()
        if len(sub_list) > 1:
            return sub_list[1]
    return None