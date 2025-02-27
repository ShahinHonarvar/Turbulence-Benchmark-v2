def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(42, 69):
        if i in lst and i % 2 == 0:
            sum += i
    return sum