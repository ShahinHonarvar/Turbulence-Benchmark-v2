def find_second_smallest_num(num_list):
    sub_list = sorted(num_list[22:51])
    if len(sub_list) < 2:
        return None
    else:
        return sub_list[1]