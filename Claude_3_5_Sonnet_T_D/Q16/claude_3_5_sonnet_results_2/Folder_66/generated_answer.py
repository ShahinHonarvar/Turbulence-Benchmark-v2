def sum_even_ints_inclusive(integer_list):
    even_sum = 0
    for i in range(50, 55):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum