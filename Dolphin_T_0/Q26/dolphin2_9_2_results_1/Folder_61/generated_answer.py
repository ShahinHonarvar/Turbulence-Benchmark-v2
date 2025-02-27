def sum_in_range(lst):
    total = 0
    for num in lst:
        if num in range(8, 10):
            total += num
    if total == 0:
        return 0
    else:
        return total