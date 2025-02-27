def find_second_smallest_num(lst):
    if len(lst) < 31 or len(lst) > 94:
        return 'None'
    else:
        lst.sort()
        return lst[30]