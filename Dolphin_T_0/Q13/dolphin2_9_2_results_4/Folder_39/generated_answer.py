def find_second_largest_num(lst):
    if 30 < len(lst) < 20:
        sublist = lst[20:31]
        if len(sublist) < 2:
            return None
        else:
            second_largest = sorted(sublist)[-2]
            return second_largest
    else:
        return None