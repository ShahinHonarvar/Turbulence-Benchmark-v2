def sum_ints_div_by_either_nums(lst):
    sum = 0
    for i in range(200, 201):
        if i == 200:
            if lst[i] % 17 == 0 or lst[i] % -5 == 0:
                sum += lst[i]
    return sum