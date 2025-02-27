def find_second_smallest_num(num_list):
    if len(num_list) > 36:
        num_list = num_list[28:39]
        return sorted(num_list)[-2]
    else:
        return None