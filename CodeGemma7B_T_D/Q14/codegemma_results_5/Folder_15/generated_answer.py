def find_second_smallest_num(lst):
    if not lst or len(lst) < 3:
        return None
    lst = sorted(lst)
    for i in range(0, 4):
        if lst[i] != lst[0]:
            return lst[i]
    return None