def find_second_smallest_num(lst):
    lst = [x for x in lst[1:101]]
    if len(lst) < 2:
        return None
    s = min(lst)
    lst.remove(s)
    if lst:
        return min(lst)
    else:
        return None