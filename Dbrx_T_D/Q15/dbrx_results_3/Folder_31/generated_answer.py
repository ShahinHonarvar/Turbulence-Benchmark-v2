def sum_odd_ints_inclusive(lst):
    if len(lst) < 88:
        return 0
    sum_val = 0
    for i in range(75, 89):
        if lst[i] % 2 != 0:
            sum_val += lst[i]
    return sum_val