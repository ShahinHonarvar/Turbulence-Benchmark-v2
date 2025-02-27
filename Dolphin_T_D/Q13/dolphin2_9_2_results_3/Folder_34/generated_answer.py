def find_second_largest_num(lst):
    if len(lst) == 0 or len(lst) < 61:
        return None
    else:
        sublist = lst[16:62]
        if len(sublist) < 2:
            return None
        else:
            sublist_sorted = sorted(sublist, reverse=True)
            second_largest_num = sublist_sorted[1]
            return second_largest_num