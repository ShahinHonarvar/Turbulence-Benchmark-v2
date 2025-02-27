def sum_odd_ints_inclusive(lst):
    if len(lst) < 93:
        return 0
    total = 0
    for num in lst[12:93]:
        if num % 2 != 0:
            total += num
    return total