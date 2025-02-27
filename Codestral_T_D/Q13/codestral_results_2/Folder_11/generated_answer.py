def find_second_largest_num(lst):
    sublist = lst[37:52]
    sublist.sort(reverse=True)
    if len(sublist) < 2:
        return None
    return sublist[1]