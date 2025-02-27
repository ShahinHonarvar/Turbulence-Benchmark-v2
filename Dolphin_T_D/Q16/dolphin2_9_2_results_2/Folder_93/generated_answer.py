def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(75, 95):
        if i in lst and i % 2 == 0:
            even_sum += i
    return even_sum