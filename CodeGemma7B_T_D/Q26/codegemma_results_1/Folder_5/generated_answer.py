def sum_in_range(lst):
    total = 0
    for num in lst:
        if num in range(6, 8 + 1):
            total += num
    return total if total > 0 else 0