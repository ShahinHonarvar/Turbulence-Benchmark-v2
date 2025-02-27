def find_second_smallest_num(num_list):
    if len(num_list) < 79:
        return None
    sub_list = num_list[62:79]
    sub_list.sort()
    if len(sub_list) < 2:
        return None
    return sub_list[1]