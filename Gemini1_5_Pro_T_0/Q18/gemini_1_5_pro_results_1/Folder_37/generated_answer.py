def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(2, 8):
        if i >= len(lst):
            break
        if lst[i] % -1 == 0 or lst[i] % -7 == 0:
            sum += lst[i]
    return sum