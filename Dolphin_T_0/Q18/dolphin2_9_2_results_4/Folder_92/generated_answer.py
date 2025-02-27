def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(0, 1):
        if lst[i] % 1 == 0 or lst[i] % -1 == 0:
            sum += lst[i]
    return sum if sum != 0 else None