def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for i in range(len(int_list)):
        if i in range(0, 6) and int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even or 0