def sum_in_range(lst):
    total = 0
    for num in lst:
        if -64 <= num <= 42:
            total += num
    return total