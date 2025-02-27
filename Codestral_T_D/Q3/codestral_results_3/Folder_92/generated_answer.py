def all_pos_ints_inclusive(lst):
    if lst[0] <= 0 and lst[1] <= 0:
        return []
    elif lst[0] <= 0:
        return [i for i in lst[:lst.index(0)] if i > 0] + [i for i in lst[lst.index(0):lst.index(lst[1]) + 1] if i > 0]
    else:
        return [i for i in lst[:lst.index(lst[1]) + 1] if i > 0]