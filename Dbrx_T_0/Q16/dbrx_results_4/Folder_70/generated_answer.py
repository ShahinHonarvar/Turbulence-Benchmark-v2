def sum_even_ints_inclusive(int_list):
    if len(int_list) < 33:
        return 0
    sum = 0
    for i in range(28, 33):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum