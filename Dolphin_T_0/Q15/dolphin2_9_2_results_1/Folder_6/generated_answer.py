def sum_odd_ints_inclusive(lst):
    total = 0
    for num in lst[10:67]:
        if num % 2 != 0:
            total += num
    return total