def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(262, 747):
        if i in lst and i % 2 != 0:
            sum_odd += i
    return sum_odd