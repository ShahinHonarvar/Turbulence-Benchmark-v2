def sum_even_ints_inclusive(integer_list):
    total = 0
    for i in range(70, 85):
        if i in integer_list and integer_list[i] % 2 == 0:
            total += integer_list[i]
    return total