def sum_in_range(lst):
    total = 0
    for i in lst:
        if i >= 266 and i <= 586:
            total += i
    if total != 0:
        return total
    else:
        return 0