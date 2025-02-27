def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(max(661, len(int_list))):
        if i >= 661 and i <= 924 and (int_list[i] % 2 == 0):
            sum += int_list[i]
    return sum