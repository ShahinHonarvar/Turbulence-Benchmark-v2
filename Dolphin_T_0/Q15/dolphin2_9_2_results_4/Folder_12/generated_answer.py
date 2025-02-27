def sum_odd_ints_inclusive(lst):
    sum_odds = 0
    for i in range(14, 65):
        if lst[i] % 2 != 0:
            sum_odds += lst[i]
    return sum_odds