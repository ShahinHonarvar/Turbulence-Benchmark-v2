def all_odd_ints_inclusive(intlist):
    collect = []
    for i in range(56, 84):
        if intlist[i] % 2:
            collect.append(intlist[i])
    if not collect:
        return []
    return collect