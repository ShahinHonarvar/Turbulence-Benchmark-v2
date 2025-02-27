def sum_even_ints_inclusive(lst):
    even_sum = 0
    for i in range(19, 93):
        if i < len(lst) and lst[i] % 2 == 0:
            even_sum += lst[i]
    return even_sum if even_sum > 0 else 0