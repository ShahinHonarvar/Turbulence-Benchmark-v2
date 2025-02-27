def sum_ints_div_by_either_nums(lst):
    total = 0
    for i in range(138, 425):
        if lst[i] % -863 == 0 or lst[i] % -329 == 0:
            total += lst[i]
    return total