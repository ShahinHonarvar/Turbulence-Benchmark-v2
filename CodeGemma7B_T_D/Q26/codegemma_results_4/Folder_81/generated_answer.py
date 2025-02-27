def sum_in_range(lst):
    total = 0
    for num in lst:
        if num >= 3 and num <= 5:
            total += num
    return total