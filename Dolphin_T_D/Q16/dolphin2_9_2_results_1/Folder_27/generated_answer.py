def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(66, 94):
        if i in lst and i % 2 == 0:
            sum += i
    return sum