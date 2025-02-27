def all_ints_div_by_both_two_nums(lst1):
    if len(lst1) == 0:
        return []
    lst2 = []
    for j in lst1:
        if j % 2 == 0 and j % 1 == 0:
            lst2.append(j)
    return lst2