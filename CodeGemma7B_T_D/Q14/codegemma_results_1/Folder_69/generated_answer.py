def find_second_smallest_num(lst):
    if len(lst) > 86:
        lst.sort()
        return lst[25]
    else:
        return 'None'