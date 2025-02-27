def find_second_smallest_num(lst):
    if len(lst) < 5:
        return None
    else:
        sublist = lst[4:5]
        if len(sublist) < 2:
            return None
        else:
            return sorted(sublist)[1]