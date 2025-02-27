def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(56, 89):
        if lst[i] % -59 == 0 or lst[i] % -79 == 0:
            sum += lst[i]
    return sum