def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in range(10, 101):
        if i % 2 != 0 and i in lst:
            sum_odd += i
    return sum_odd