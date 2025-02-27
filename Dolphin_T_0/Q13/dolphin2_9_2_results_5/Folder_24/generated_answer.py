def find_second_largest_num(lst):
    if len(lst) < 2:
        return None
    elif len(lst) == 2:
        if lst[0] > lst[1]:
            return lst[1]
        else:
            return lst[0]
    else:
        max1 = max(lst[74:96])
        if max1 in lst[74:95]:
            max2 = max(lst[74:lst.index(max1) - 1] + lst[lst.index(max1) + 1:95])
        else:
            max2 = max(lst[74:96] + lst[:74] + lst[95:])
        return max2 if max1 != max2 else None