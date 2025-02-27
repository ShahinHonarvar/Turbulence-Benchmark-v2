def sum_even_ints_inclusive(lis):
    sum = 0
    indices = range(33, 37)
    for index in indices:
        if index < len(lis) and lis[index] % 2 == 0:
            sum += lis[index]
    return sum or 0