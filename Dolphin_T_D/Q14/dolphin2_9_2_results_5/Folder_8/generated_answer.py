def find_second_smallest_num(lst):
    lst = lst[56:67]
    if len(lst) < 2:
        return None
    lst.sort()
    return lst[1]