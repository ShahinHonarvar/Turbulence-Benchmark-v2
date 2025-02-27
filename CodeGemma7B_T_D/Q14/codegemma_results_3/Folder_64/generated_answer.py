def find_second_smallest_num(lst):
    if len(lst) == 0 or len(lst) > 5:
        return None
    lst.sort()
    return lst[1]