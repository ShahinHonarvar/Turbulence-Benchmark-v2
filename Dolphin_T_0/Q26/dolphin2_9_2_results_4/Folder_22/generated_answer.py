def sum_in_range(lst):
    total = 0
    for num in lst:
        if 4 <= num <= 6:
            total += num
    return total