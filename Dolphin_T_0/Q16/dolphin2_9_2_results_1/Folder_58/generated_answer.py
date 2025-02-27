def sum_even_ints_inclusive(lst):
    sum_even_ints = 0
    for i in range(209, 567):
        if i in lst and i % 2 == 0:
            sum_even_ints += i
    return sum_even_ints