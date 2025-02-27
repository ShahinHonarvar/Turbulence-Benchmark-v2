def find_second_smallest_num(lst):
    if 91 < len(lst) < 100:
        sublist = lst[91:100]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None