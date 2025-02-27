def sum_ints_div_by_either_nums(ls):
    sum = 0
    for i in range(154, 799):
        if ls[i] % 275 == 0 or ls[i] % 580 == 0:
            sum += ls[i]
    return sum if sum != 0 else 0