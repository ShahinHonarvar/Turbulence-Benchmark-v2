def sum_even_ints_inclusive(lst):
    even_ints_sum = 0
    for i in range(661, 925):
        if i < len(lst) and lst[i] % 2 == 0:
            even_ints_sum += lst[i]
    return even_ints_sum