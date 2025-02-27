def find_second_smallest_num(num_list):
    if 370 < len(num_list):
        sublist = num_list[310:371]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[1]
    return None