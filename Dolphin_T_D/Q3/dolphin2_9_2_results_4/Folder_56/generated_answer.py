def all_pos_ints_inclusive(lst):
    if lst[0] < 0 and lst[1] < 0:
        return []
    elif lst[0] < 0:
        return list(range(0, lst[1] + 1))
    elif lst[1] < 0:
        return list(range(lst[0], 0))
    else:
        return list(range(lst[0], lst[1] + 1))