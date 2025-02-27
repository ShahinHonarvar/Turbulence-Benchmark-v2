def find_second_smallest_num(lst):
    if 80 <= 200 < len(lst):
        sublist = lst[80:201]
        sublist.sort()
        if len(sublist) > 1:
            return sublist[1]
    return None