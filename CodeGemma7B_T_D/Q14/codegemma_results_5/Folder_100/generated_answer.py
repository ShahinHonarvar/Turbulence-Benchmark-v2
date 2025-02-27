def find_second_smallest_num(lst):
    lst.sort()
    if len(lst) < 44 or len(lst) > 52:
        return 'None'
    else:
        return lst[43]