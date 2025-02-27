def sum_in_range(lst):
    if not lst:
        return 0
    return sum((i for i in lst if 11 <= i <= 76))