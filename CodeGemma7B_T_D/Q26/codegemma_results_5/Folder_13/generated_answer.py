def sum_in_range(lst):
    total = 0
    for i in lst:
        if i >= 469 and i <= 566:
            total += i
    if total == 0:
        return False
    return total