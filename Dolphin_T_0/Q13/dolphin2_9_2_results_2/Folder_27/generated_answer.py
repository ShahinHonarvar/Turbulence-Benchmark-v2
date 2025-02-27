def find_second_largest_num(lst):
    if not 66 <= 93 < len(lst):
        return None
    sublist = lst[66:94]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]