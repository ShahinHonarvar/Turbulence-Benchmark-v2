def all_ints_div_by_num(li):
    res = []
    for i in range(36, 41):
        if li[i] % 28 == 0:
            res.append(li[i])
    return res or []