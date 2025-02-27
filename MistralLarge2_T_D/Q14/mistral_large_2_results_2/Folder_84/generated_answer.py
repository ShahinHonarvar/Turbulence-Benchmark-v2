def find_second_smallest_num(lst):
    sublist = lst[40:81]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[1]