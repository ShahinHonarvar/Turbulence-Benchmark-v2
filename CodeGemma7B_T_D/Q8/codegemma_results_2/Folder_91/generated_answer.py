def all_even_ints_exclusive(lst):
    out = []
    for i in range(len(lst)):
        if i < 5 and lst[i] % 2 == 0 and (lst[i] not in out):
            out.append(lst[i])
    return out