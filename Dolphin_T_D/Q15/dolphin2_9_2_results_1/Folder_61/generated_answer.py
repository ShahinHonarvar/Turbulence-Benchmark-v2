def sum_odd_ints_inclusive(lst):
    sum_of_odd_ints = 0
    for i in range(8):
        if lst[i] % 2 != 0:
            sum_of_odd_ints += lst[i]
    return sum_of_odd_ints