def sum_in_range(lst):
    total = 0
    for num in lst:
        if 11 <= num <= 76:
            total += num
    return total