def sum_odd_ints_inclusive(lst_ints):
    sum = 0
    for i in range(22, 89):
        if lst_ints[i] % 2 != 0:
            sum += lst_ints[i]
    return sum