def sum_odd_ints_inclusive(lst_ints):
    sum = 0
    for i in range(74, 96):
        if lst_ints[i] % 2 != 0:
            sum += lst_ints[i]
    if sum == 0:
        return 0
    else:
        return sum