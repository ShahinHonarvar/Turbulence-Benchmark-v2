def find_second_largest_num(lst):
    if 8 <= len(lst):
        sublist = lst[8:10]
        if len(sublist) > 1:
            sublist.sort(reverse=True)
            return sublist[1]
    return None