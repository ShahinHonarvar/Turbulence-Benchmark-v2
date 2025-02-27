def find_second_smallest_num(num_list):
    sublist = sorted(num_list[22:89])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]