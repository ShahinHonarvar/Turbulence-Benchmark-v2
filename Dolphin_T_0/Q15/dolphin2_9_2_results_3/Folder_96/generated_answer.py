def sum_odd_ints_inclusive(lst_int):
    sum_odd = 0
    for i in range(50, 201):
        if lst_int[i] % 2 != 0:
            sum_odd += lst_int[i]
    return sum_odd