def find_second_largest_num(lst):
    if len(lst) < 247 or len(lst) < 751:
        sliced_list = lst[246:751]
        if len(sliced_list) < 2:
            return None
        else:
            sliced_list.sort()
            return sliced_list[-2]
    else:
        return None