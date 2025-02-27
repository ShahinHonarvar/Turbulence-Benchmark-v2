def sum_odd_ints_inclusive(lst):
    sum = 0
    for i in range(20, 201):
        if lst[i] % 2 == 1:
            sum += lst[i]
    return sum