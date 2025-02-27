def find_second_largest_num(lst):
    if len(lst) < 200:
        return None
    lst = lst[19:201]
    lst.sort()
    if len(lst) < 2:
        return None
    return lst[-2]