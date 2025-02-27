def sum_odd_ints_inclusive(lst):
    if len(lst) < 30:
        return 0
    total = 0
    for num in lst[29:52]:
        if num % 2 != 0:
            total += num
    return total