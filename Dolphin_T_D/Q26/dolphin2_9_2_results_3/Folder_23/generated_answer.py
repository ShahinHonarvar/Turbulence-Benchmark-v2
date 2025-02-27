def sum_in_range(lst):
    total = 0
    for num in lst:
        if 50 <= num <= 92:
            total += num
    return total