def sum_in_range(lst):
    total = 0
    for item in lst:
        if -97 <= item <= -48:
            total += item
    return total