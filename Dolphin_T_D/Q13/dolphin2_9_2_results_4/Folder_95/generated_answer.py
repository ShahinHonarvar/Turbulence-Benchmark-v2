def find_second_largest_num(num_list):
    if 82 > len(num_list) or 86 < len(num_list):
        return None
    else:
        sublist = num_list[82:87]
        sublist.sort()
        return sublist[3]