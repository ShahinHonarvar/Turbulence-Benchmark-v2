def sum_in_range(lst):
    total = 0
    for i in lst:
        if 3 <= i <= 9:
            total += i
    return total if total != 0 else 0