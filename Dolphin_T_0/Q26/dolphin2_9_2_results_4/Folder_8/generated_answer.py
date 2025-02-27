def sum_in_range(lst):
    total = 0
    for i in lst:
        if -33 <= i <= 93:
            total += i
    return total if total != 0 else None