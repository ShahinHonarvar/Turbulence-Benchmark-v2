def sum_odd_ints_inclusive(l):
    sum = 0
    for i in range(4, 9):
        if l[i] % 2 == 1:
            sum += l[i]
    return sum if sum else 0