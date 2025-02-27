def all_even_ints_exclusive(lst):
    ret = []
    for i in range(88, 96):
        if i < len(lst) and lst[i] % 2 == 0:
            ret.append(lst[i])
    return ret