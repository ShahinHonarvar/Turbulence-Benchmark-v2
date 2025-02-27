def sum_even_ints_inclusive(lst):
    sum_of_even_ints = 0
    for i in range(64, 67):
        if i < len(lst) and lst[i] % 2 == 0:
            sum_of_even_ints += lst[i]
    return sum_of_even_ints