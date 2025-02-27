def sum_odd_ints_inclusive(lst):
    if not lst:
        return 0
    sum_of_odds = 0
    for i in range(22, 51):
        if i % 2 != 0 and i < len(lst):
            sum_of_odds += lst[i]
    return sum_of_odds