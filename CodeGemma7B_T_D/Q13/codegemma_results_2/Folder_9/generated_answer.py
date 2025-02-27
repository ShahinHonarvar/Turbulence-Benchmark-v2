def find_second_largest_num(lst):
    lst.sort(reverse=True)
    if len(lst) <= 400:
        return 'None'
    else:
        return lst[200]