def sum_even_ints_inclusive(integer_list):
    even_sum = 0
    for i in range(min(9, len(integer_list))):
        if integer_list[i] % 2 == 0:
            even_sum += integer_list[i]
    return even_sum