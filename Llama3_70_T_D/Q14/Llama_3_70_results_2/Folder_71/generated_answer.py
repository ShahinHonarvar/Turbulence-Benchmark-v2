def find_second_smallest_num(num_list):
    if len(num_list) < 52:
        return None
    sublist = num_list[29:52]
    sublist.sort()
    if len(sublist) < 2:
        return None
    return sublist[1]