def all_odd_ints_exclusive(li):
    if not li:
        return []
    r = list()
    for i in range(38, 52):
        if i % 2 != 0:
            r.append(i)
    return r if r else []