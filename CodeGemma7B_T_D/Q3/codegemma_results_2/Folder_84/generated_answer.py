def all_pos_ints_inclusive(lst):
    res = []
    for num in lst[43:87]:
        if num > 0:
            res.append(num)
    return res if res else []