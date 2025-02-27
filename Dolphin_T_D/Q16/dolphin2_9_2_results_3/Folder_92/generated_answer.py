def sum_even_ints_inclusive(int_list):
    sum = 0
    if int_list[0] % 2 == 0:
        sum += int_list[0]
    if int_list[1] % 2 == 0:
        sum += int_list[1]
    return sum