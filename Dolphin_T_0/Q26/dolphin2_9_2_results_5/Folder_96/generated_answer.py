def sum_in_range(lst):
    total = 0
    for num in lst:
        if 4 <= num <= 8:
            total += num
    return total if total > 0 else 0