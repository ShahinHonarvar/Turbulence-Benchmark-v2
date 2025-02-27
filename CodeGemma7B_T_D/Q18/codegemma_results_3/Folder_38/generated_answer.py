def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(10, 77):
        if lst[i] % 40 == 0 or lst[i] % 12 == 0:
            total += lst[i]
    return total if total else 0