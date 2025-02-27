def sum_even_ints_inclusive(lst):
    sum_even_ints = 0
    for i in range(50, 55):
        if i < len(lst) and lst[i] % 2 == 0:
            sum_even_ints += lst[i]
    return sum_even_ints