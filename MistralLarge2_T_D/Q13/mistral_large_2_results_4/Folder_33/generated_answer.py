def find_second_largest_num(lst):
    if len(lst) < 775:
        return None
    sublist = lst[667:775]
    if len(sublist) < 2:
        return None
    sublist.sort()
    return sublist[-2]