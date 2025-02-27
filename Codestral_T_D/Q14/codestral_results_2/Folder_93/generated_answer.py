def find_second_smallest_num(num_list):
    sub_list = sorted(num_list[75:89])
    if len(sub_list) > 1:
        return sub_list[1]
    return None