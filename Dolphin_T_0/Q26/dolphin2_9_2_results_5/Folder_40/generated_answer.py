def sum_in_range(lst):
    total = 0
    for i in lst:
        if i >= -9 and i <= -7:
            total += i
    return total if total != 0 else 0