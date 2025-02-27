def find_second_smallest_num(lst):
    if len(lst) < 11:
        return None
    lst.sort()
    return lst[10]