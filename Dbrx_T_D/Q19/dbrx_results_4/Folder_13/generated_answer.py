def all_ints_not_div_by_num(lst):
    if len(lst) < 44:
        return []
    notasdivisible = []
    for i in range(32, 44):
        num = lst[i]
        if num % 34 != 0:
            notasdivisible.append(num)
    return notasdivisible