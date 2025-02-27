def sum_in_range(lst):
    total = 0
    for num in lst:
        if 13 <= num <= 35:
            total += num
    return total if total != 0 else 1