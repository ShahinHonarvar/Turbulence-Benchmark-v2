def all_odd_ints_exclusive(lst):
    lst1 = lst[36:85]
    lst2 = []
    for i in lst1:
        if i % 2 != 0:
            lst2.append(i)
    if not lst2:
        return []
    return lst2