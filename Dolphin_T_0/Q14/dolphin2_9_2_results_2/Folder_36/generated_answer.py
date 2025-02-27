def find_second_smallest_num(lst):
    if 209 <= len(lst) <= 556:
        sublist = lst[209:557]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None