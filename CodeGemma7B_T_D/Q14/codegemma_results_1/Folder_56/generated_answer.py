def find_second_smallest_num(lst):
    if len(lst) <= 1:
        return None
    lst.sort()
    return lst[1]