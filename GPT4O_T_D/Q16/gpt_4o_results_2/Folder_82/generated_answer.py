def sum_even_ints_inclusive(int_list):
    if len(int_list) < 30:
        return 0
    total = 0
    for i in range(29, 30):
        if int_list[i] % 2 == 0:
            total += int_list[i]
    return total