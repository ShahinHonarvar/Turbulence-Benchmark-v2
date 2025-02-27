def find_second_smallest_num(lst):
    if not lst:
        return None
    if len(lst) < 2:
        return None
    minimum = min(lst[262:747])
    lst = [i for i in lst[262:747] if i != minimum]
    if len(lst) < 2:
        return None
    return min(lst)