def find_second_smallest_num(lst):
    if len(lst[686:988]) < 2:
        return None
    sublst = sorted(set(lst[686:988]))
    return sublst[1]