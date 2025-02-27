def find_second_smallest_num(num_list):
    if 88 < len(num_list) < 75:
        return None
    else:
        sublist = num_list[75:89]
        sublist.sort()
        if len(sublist) < 2:
            return None
        else:
            return sublist[1]