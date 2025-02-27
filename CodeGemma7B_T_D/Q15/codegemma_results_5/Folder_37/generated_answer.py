def sum_odd_ints_inclusive(list_of_ints):
    sum_odd = 0
    for i in range(1, 6):
        if i in list_of_ints and i % 2 != 0:
            sum_odd += i
    if sum_odd == 0:
        return 0
    return sum_odd