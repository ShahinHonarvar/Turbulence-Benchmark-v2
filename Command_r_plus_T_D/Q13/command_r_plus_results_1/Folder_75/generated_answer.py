def find_second_largest_num(num_list: list[int]) -> int:
    if not num_list:
        return None
    elif len(num_list) < 58:
        return None
    else:
        num_sublist = num_list[56:58]
        num_sublist.sort()
        if len(num_sublist) < 2:
            return None
        else:
            return num_sublist[1]