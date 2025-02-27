def sum_odd_ints_inclusive(lst_of_ints):
    sum_ = 0
    for i in range(30, 88):
        if lst_of_ints[i] % 2 != 0:
            sum_ += lst_of_ints[i]
    return sum_