def sum_in_range(lst):
    if not lst:
        return 0
    total = 0
    for num in lst:
        if 32 <= num <= 44:
            total += num
    return total