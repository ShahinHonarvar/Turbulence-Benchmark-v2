def find_second_largest_num(lst):
    sublst = lst[91:100]
    if len(sublst) < 2:
        return None
    max1 = max(sublst)
    sublst.remove(max1)
    if not sublst:
        return None
    max2 = max(sublst)
    return max2