def sum_even_ints_inclusive(numlist):
    sum_even = 0
    for i in range(28, 33):
        if numlist[i] % 2 == 0:
            sum_even += numlist[i]
    return sum_even