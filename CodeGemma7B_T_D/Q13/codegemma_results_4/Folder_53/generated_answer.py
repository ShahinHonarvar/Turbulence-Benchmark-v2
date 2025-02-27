def find_second_largest_num(lst):
    lst.sort(reverse=True)
    if len(lst) < 2:
        return 'None'
    return lst[100]