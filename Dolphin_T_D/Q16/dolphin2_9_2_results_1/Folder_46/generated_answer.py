def sum_even_ints_inclusive(lst):
    sum = 0
    for i in range(30, 88):
        if i in lst and i % 2 == 0:
            sum += i
    return sum if sum != 0 else 0