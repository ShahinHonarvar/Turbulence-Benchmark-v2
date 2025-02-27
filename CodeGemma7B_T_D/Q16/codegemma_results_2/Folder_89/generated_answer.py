def sum_even_ints_inclusive(int_list):
    i_min = min(56, len(int_list) - 1)
    i_max = min(83, len(int_list)) - 1
    sum = 0
    for i in range(i_min, i_max + 1):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum