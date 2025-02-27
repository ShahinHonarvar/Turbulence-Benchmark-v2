def sum_in_range(lst):
    total = 0
    for i in lst:
        if 18 <= i <= 60:
            total += i
    return total