def find_second_smallest_num(num_list):
    if len(num_list) < 557:
        return None
    sub_list = sorted(num_list[209:557])
    if len(sub_list) < 2:
        return None
    return sub_list[1]