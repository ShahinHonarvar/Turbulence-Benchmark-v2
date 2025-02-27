def find_second_largest_num(lst):
    lst = lst[75:95]
    if len(lst) > 1:
        lst.sort(reverse=True)
        return lst[1]
    else:
        return 'None'