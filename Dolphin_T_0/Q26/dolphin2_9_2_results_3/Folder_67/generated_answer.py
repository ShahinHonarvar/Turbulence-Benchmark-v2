def sum_in_range(lst):
    total = 0
    for num in lst:
        if num in range(31, 51):
            total += num
    return total