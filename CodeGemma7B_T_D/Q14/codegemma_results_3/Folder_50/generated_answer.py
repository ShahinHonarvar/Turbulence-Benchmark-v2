def find_second_smallest_num(lst):
    lst = sorted(lst)
    if len(lst) < 43 or not 42 <= lst.index(lst[42]) <= 68:
        return 'None'
    return lst[43]