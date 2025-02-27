def all_ints_not_div_by_num(list):
    L = []
    for i in range(13, 70):
        if list[i] % -78 != 0:
            L.append(list[i])
    return L if len(L) > 0 else []