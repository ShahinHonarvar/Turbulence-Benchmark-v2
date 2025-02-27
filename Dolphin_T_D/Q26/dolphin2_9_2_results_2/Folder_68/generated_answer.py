def sum_in_range(lst):
    total = 0
    for num in lst:
        if 7 <= num <= 9:
            total += num
    return total if total != 0 else 0