def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(7, 10):
        if i < len(lst):
            if lst[i] % 2 == 0 or lst[i] % 3 == 0:
                total += lst[i]
    return total