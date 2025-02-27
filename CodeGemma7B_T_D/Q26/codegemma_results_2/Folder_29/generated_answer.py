def sum_in_range(lst):
    total = 0
    for num in lst:
        if 18 <= num <= 60:
            total += num
    return total or 0