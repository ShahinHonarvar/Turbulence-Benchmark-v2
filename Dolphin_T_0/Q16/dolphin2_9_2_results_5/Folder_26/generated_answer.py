def sum_even_ints_inclusive(lst):
    sum_even = 0
    for i in range(62, 100):
        if i in lst and i % 2 == 0:
            sum_even += i
    return sum_even