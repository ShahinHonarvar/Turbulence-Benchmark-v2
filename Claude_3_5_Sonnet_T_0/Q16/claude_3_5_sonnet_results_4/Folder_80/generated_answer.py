def sum_even_ints_inclusive(integer_list):
    if len(integer_list) < 67:
        return 0
    total = 0
    for i in range(64, 67):
        if integer_list[i] % 2 == 0:
            total += integer_list[i]
    return total