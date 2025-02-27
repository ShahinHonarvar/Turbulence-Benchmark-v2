def sum_ints_div_by_either_nums(ints):
    sum = 0
    for i in range(10):
        if ints[i] % 6 == 0 or ints[i] % -3 == 0:
            sum += ints[i]
    return sum if sum != 0 else None