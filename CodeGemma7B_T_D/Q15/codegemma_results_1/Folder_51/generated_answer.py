def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(1, 9):
        if i in lst and i % 2:
            sum += i
    return sum if sum else 0