def sum_in_range(lst):
    total = 0
    for i in lst:
        if i >= 43 and i <= 70:
            total += i
    return total if total else 0