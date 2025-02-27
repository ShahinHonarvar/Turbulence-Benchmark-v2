def all_pos_ints_inclusive(lst):
    res = []
    if not any(lst):
        return res
    pos_min, pos_max = (next((i for i, x in enumerate(lst) if x > 0), None), next((i for i, x in enumerate(lst) if x > 0), None))
    if pos_min is None or pos_max is None:
        return res
    for i in range(pos_min, pos_max + 1):
        res.append(i)
    return res