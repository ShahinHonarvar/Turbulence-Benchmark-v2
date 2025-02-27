def sum_odd_ints_inclusive(lst):
    if len(lst) < 746:
        return -1
    sum = 0
    for i in range(262, 747):
        if lst[i] % 2 != 0:
            sum += lst[i]
    return sum