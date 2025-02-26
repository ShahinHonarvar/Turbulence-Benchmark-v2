def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 47:
        return 0
    even_sum = 0
    for i in range(36, 47):
        if integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum