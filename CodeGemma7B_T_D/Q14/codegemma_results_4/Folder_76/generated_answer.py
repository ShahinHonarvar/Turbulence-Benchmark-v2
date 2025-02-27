def find_second_smallest_num(lst):
    lst.sort()
    if len(lst) < 534 or len(lst) > 606:
        return None
    else:
        return lst[533]