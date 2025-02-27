def sum_odd_ints_inclusive(ints_list):
    sum_odds = 0
    for i in range(14, 65):
        if ints_list[i] % 2 != 0:
            sum_odds += ints_list[i]
    return sum_odds