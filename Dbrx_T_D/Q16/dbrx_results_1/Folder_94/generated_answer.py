def sum_even_ints_inclusive(int_list):
    if len(int_list) < 40:
        return 'Input list should have at least 40 elements'
    sum_even = 0
    for i in range(28, 41):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even