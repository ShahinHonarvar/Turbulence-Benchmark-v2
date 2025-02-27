def sum_odd_ints_inclusive(lst):
    sum_odd = 0
    for i in lst[22:64]:
        if i % 2 != 0:
            sum_odd += i
    return sum_odd or 0