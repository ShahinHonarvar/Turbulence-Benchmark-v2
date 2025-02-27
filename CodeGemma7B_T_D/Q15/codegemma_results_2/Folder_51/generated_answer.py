def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(1, 9):
        if i in lst and i % 2 != 0:
            sum += i
    if sum == 0:
        return 0
    return sum