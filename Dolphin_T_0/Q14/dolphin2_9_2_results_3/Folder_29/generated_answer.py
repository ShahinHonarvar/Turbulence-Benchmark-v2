def find_second_smallest_num(lst):
    if 98 >= len(lst) >= 55:
        from_index = 55
        to_index = 98
    else:
        return None
    sublist = sorted(lst[from_index:to_index + 1])
    if len(sublist) < 2:
        return None
    if sublist[1] != sublist[0]:
        return sublist[1]
    for i in range(2, len(sublist)):
        if sublist[i] != sublist[i - 1]:
            return sublist[i]
    return None