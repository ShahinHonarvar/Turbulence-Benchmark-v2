def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(17, 79):
        if i in lst and i % 2 != 0:
            sum += i
    return sum