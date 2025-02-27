def sum_even_ints_inclusive(int_list):
    sum = 0
    for i in range(14, 65):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum