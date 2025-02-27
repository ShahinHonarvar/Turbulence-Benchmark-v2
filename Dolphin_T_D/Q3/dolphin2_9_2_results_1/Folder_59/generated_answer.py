def all_pos_ints_inclusive(lst):
    lst = [num for num in lst[0:10] if num > 0]
    if len(lst) == 0:
        return []
    else:
        return lst