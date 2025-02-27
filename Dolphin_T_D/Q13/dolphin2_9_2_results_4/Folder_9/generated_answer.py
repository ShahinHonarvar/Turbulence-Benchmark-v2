def find_second_largest_num(lst):
    if 200 < len(lst):
        sublist = lst[200:201]
        if len(sublist) > 1:
            sublist.sort()
            return sublist[1]
    return None