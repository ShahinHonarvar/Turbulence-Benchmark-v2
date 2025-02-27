def sum_in_range(lst):
    total = 0
    for integer in lst:
        if 86 <= integer <= 90:
            total += integer
    return total if total != 0 else 0