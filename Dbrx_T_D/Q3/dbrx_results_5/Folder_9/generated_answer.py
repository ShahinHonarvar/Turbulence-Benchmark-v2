def all_pos_ints_inclusive(lst):
    if len(lst) < 200:
        return []
    result = lst[70:201]
    return [i for i in result if i > 0]