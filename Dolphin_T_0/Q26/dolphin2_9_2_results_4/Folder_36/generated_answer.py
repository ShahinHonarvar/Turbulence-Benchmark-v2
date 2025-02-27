def sum_in_range(lst):
    total = 0
    for i in lst:
        if i >= 465 and i <= 927:
            total += i
    return total if total != 0 else 0