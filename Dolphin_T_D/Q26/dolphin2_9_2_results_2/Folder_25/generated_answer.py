def sum_in_range(lst):
    total = 0
    for i in lst:
        if -10 <= i <= 48:
            total += i
    return total if total else 0