def sum_in_range(lst):
    total = 0
    for i in lst:
        if i >= 5 and i <= 8:
            total += i
    return total if total else 0