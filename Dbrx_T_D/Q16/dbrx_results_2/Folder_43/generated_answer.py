def sum_even_ints_inclusive(integer_list):
    sum = 0
    for i in range(min(68, len(integer_list)), min(87, len(integer_list))):
        if integer_list[i] % 2 == 0:
            sum += integer_list[i]
    return sum