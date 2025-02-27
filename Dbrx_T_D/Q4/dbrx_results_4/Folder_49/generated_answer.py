def all_pos_ints_exclusive(lst):
    if len(lst) <= 200 or len(lst) < 80:
        return []
    else:
        return [i for i in lst[80:200] if i > 0]