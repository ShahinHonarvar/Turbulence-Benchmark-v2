def sum_in_range(num):
    total = 0
    for x in num:
        if x >= 44 and x <= 67:
            total += x
    return total or 0