def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(27, 56):
        if i < len(lst) and lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum