def sum_in_range(lst):
    total = 0
    for i in lst:
        if i >= 28 and i <= 96:
            total += i
    return total or 0