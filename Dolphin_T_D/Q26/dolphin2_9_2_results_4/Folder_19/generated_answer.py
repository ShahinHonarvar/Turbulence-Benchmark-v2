def sum_in_range(lst):
    total = 0
    for i in lst:
        if 7 <= i <= 8:
            total += i
    return total if total != 0 else 0