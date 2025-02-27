def sum_in_range(lst):
    total = 0
    for num in lst:
        if num in range(-100, -55):
            total += num
    return total