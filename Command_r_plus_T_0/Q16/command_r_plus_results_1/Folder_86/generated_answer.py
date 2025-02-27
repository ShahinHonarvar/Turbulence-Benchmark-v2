def sum_even_ints_inclusive(int_list):
    even_sum = 0
    for i in range(31, 35):
        if int_list[i] % 2 == 0:
            even_sum += int_list[i]
    return even_sum