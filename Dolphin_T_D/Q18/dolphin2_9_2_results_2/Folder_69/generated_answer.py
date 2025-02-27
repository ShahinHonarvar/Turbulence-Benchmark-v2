def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(61, 89):
        if lst[i] % 31 == 0 or lst[i] % 11 == 0:
            total += lst[i]
    return total if total != 0 else 0