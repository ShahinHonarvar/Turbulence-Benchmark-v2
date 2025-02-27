def find_second_smallest_num(lst):
    if 50 <= len(lst) <= 200:
        sublist = sorted(lst[50:201])
        if len(sublist) > 1:
            return sublist[1]
    return None