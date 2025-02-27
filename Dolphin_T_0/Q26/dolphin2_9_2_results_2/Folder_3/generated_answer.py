def sum_in_range(lst):
    total = 0
    for i in lst:
        if 38 <= i <= 81:
            total += i
    return total if total != 0 else None