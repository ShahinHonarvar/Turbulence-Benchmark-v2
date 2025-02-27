def sum_in_range(lst):
    total = 0
    for num in lst:
        if num >= 10 and num <= 97:
            total += num
    return total