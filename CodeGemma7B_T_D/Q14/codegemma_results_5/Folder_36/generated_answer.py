def find_second_smallest_num(lst):
    if len(lst) < 209 or len(lst) > 556:
        return None
    lst = lst[209:557]
    lst.sort()
    if len(lst) < 2:
        return None
    return lst[1]