def sum_in_range(lst):
    total = 0
    for num in lst:
        if num >= 136 and num <= 618:
            total += num
    return total