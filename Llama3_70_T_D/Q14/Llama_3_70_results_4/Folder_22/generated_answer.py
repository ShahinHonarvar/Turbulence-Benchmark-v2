def find_second_smallest_num(num_list):
    sublist = sorted(num_list[40:201])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]