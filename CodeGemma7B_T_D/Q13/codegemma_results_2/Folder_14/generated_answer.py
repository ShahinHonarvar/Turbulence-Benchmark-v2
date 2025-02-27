def find_second_largest_num(lst):
    if len(lst) < 8:
        return 'None'
    else:
        lst.sort(reverse=True)
        return lst[7]