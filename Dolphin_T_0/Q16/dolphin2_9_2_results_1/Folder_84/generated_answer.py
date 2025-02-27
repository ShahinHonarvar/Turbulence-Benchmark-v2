def sum_even_ints_inclusive(int_list):
    result = 0
    for i in range(43, 87):
        if int_list[i] % 2 == 0:
            result += int_list[i]
    return result