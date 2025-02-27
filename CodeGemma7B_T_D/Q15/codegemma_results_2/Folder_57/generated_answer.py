def sum_odd_ints_inclusive(list):
    sum = 0
    for i in range(27, 56):
        if list[i] % 2 != 0:
            sum += list[i]
    if sum == 0:
        return 0
    return sum