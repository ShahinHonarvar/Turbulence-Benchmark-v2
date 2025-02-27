def find_second_largest_num(lst):
    s = sorted(lst)
    if len(s) == 0:
        return 'None'
    elif len(s) > 7:
        return s[-8]
    else:
        return 'None'