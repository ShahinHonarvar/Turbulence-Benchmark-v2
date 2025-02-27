def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(28, 97):
        if lst[i] % 90 == 0 or lst[i] % 97 == 0:
            total += lst[i]
    return total