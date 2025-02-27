def sum_odd_ints_inclusive(lst):
    sum_odds = 0
    for i in lst[0:8]:
        if i % 2 != 0:
            sum_odds += i
    return sum_odds