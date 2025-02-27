def sum_in_range(lst):
    total = 0
    for i in lst:
        if 8 <= i <= 9:
            total += i
    return total if total else 0