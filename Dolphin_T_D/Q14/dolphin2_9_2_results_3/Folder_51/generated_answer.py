def find_second_smallest_num(lst):
    if len(lst) < 2 or len(lst) > 8:
        return None
    lst.sort()
    return lst[1]