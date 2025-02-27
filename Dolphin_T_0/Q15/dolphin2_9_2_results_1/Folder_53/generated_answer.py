def sum_odd_ints_inclusive(lst_ints):
    sum_odd_ints = 0
    for i in range(300, 301):
        if lst_ints[i] % 2 != 0:
            sum_odd_ints += lst_ints[i]
    return sum_odd_ints