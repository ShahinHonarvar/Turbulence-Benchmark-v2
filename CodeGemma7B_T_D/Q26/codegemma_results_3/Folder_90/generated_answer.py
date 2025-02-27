def sum_in_range(lst):
    sum_in_rng = 0
    for i in lst:
        if 273 <= i <= 451:
            sum_in_rng += i
    return sum_in_rng if sum_in_rng else 0