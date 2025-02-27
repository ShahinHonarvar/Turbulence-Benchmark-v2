def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(6):
        if i >= 0 and i <= 5 and (int_list[i] % 2 == 0):
            sum += int_list[i]
    return sum