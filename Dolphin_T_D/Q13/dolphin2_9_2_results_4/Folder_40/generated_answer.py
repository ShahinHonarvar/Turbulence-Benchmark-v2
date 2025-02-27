def find_second_largest_num(lst):
    if len(lst) < 3:
        return None
    else:
        sublist = lst[0:3]
        sublist.sort()
        return sublist[1]