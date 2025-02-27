def sum_in_range(lst):
    total = 0
    for i in lst:
        if 2 <= i <= 4:
            total += i
    return total