def find_second_smallest_num(lst):
    if 200 <= len(lst) < 90:
        return None
    else:
        sublst = lst[90:201]
        sublst.sort()
        if len(sublst) < 2:
            return None
        else:
            return sublst[1]