def find_second_smallest_num(num_list):
    if len(num_list) < 69:
        return None
    sublist = sorted(num_list[13:69])
    if len(sublist) < 2:
        return None
    return sublist[1]