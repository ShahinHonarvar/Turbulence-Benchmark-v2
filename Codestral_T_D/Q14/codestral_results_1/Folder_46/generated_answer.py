def find_second_smallest_num(num_list):
    sub_list = sorted(num_list[13:69])
    if len(sub_list) >= 2:
        return sub_list[1]
    else:
        return None