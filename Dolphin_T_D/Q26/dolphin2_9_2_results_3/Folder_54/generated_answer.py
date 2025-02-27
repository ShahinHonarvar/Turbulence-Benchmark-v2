def sum_in_range(lst):
    total = 0
    for num in lst:
        if -100 <= num <= -55:
            total += num
    return total if total != 0 else None