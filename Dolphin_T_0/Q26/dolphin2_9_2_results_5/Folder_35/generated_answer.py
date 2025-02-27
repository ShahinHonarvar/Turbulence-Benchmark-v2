def sum_in_range(lst):
    total = 0
    for i in lst:
        if 139 <= i <= 767:
            total += i
    if total == 0:
        return 0
    else:
        return total