def find_second_smallest_num(num_list):
    sub_list = sorted(num_list[59:98])
    if len(sub_list) < 2:
        return None
    return sub_list[1]