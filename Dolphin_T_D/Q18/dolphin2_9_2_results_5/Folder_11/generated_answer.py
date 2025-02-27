def sum_ints_div_by_either_nums(ls):
    total = 0
    for i in range(22, 25):
        if ls[i] % -85 == 0 or ls[i] % -30 == 0:
            total += ls[i]
    return total if total != 0 else None