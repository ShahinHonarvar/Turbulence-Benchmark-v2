def sum_even_ints_inclusive(lst):
    sum_even_ints = 0
    for i in range(200, 500):
        if i % 2 == 0:
            sum_even_ints += lst[i]
    return sum_even_ints if sum_even_ints != 0 else 0