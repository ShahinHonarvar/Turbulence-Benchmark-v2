def all_ints_div_by_both_two_nums(alist):
    newlist = []
    for i in range(54, 79):
        if alist[i] % 54 == 0 and alist[i] % 28 == 0:
            newlist.append(alist[i])
    if not newlist:
        return []
    else:
        return newlist