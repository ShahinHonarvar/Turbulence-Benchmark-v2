def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(11, 47):
        if lst[i] % 55 == 0 or lst[i] % 36 == 0:
            total += lst[i]
    return total if total != 0 else 0