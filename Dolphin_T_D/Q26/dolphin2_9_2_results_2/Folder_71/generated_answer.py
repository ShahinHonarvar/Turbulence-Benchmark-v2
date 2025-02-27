def sum_in_range(lst):
    total = 0
    for num in lst:
        if 39 <= num <= 43:
            total += num
    if total == 0:
        return 0
    else:
        return total