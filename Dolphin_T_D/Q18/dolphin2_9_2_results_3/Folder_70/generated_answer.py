def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(42, 44):
        if i < len(lst):
            if lst[i] % 15 == 0 or lst[i] % 87 == 0:
                total += lst[i]
    return total