def sum_in_range(lst):
    total = 0
    for i in lst:
        if 50 <= i <= 92:
            total += i
    return total if total else 0