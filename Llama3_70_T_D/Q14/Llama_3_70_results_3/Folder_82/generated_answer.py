def find_second_smallest_num(num_list):
    if len(num_list) < 201:
        return None
    sub_list = sorted(num_list[20:201])
    if len(sub_list) < 2 or sub_list[0] == sub_list[1]:
        return None
    return sub_list[1]