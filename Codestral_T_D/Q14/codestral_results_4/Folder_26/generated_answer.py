def find_second_smallest_num(lst):
    sublist = sorted(lst[62:79])
    if len(sublist) < 2:
        return None
    else:
        return sublist[1]