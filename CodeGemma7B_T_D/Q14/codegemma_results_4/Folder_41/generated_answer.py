def find_second_smallest_num(lst):
    if len(lst) <= 4:
        return 'None'
    lst.sort()
    return lst[5] if len(lst) > 5 else 'None'