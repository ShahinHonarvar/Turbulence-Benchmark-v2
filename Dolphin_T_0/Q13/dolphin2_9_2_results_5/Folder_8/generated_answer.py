def find_second_largest_num(input_list):
    if 23 < len(input_list):
        sublist = input_list[23:24]
        if len(sublist) == 2:
            sublist.sort()
            return sublist[1]
    return None