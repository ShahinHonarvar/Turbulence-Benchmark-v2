def sum_in_range(lst):
    total = 0
    for i in lst:
        if -91 <= i <= -61:
            total += i
    return total if total != 0 else 0