def sum_odd_ints_inclusive(lst):
    if len(lst) <= 6:
        return 0
    total = 0
    for num in lst[6:7]:
        if num % 2 != 0:
            total += num
    return total