def find_second_smallest_num(lst):
    sublst = lst[56:58]
    if len(sublst) == 1:
        return sublst[0]
    elif len(sublst) > 1:
        sorted_sublst = sorted(sublst)
        return sorted_sublst[1]
    else:
        return None