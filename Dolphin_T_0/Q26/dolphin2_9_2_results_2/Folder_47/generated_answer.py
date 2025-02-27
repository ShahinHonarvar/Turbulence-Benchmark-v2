def sum_in_range(lst):
    total = 0
    for i in lst:
        if 86 <= i <= 99:
            total += i
    if total == 0:
        return 0
    else:
        return total