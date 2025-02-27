def sum_even_ints_inclusive(list):
    even_sum = 0
    for i in range(29, 94):
        if i % 2 == 0:
            even_sum += list[i]
    return even_sum