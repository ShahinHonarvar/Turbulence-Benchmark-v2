def find_second_largest_num(lst):
    if len(lst) < 60 or len(lst) > 98:
        return 'None'
    lst.sort(reverse=True)
    if lst[59] == lst[97]:
        return 'None'
    return lst[59]