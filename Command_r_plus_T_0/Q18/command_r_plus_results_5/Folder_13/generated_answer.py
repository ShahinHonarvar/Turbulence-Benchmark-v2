def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(13, 19):
        if lst[i] % 45 == 0 or lst[i] % 20 == 0:
            sum += lst[i]
    return sum