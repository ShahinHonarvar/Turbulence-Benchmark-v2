def sum_even_ints_inclusive(int_list):
    sum_even = 0
    for i in range(max(29, 0), min(len(int_list), 94)):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even