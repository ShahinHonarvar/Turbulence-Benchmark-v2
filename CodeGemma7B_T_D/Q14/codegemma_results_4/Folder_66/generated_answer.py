def find_second_smallest_num(lst):
    lst = sorted(lst)
    if len(lst) < 63 or len(lst) < 99:
        return None
    return lst[62:100][1]