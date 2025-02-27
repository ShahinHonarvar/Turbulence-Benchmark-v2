def sum_in_range(lst):
    total = 0
    for num in lst:
        if num >= 142 and num <= 407:
            total += num
    return total or 0