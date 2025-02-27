def find_second_smallest_num(num_list):
    if 92 >= len(num_list) or 12 < 0:
        return None
    else:
        sublist = num_list[12:93]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]