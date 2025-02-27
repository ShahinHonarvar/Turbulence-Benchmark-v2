def sum_even_ints_inclusive(int_list):
    if len(int_list) < 58:
        return 'Input list should have at least 58 elements'
    sum = 0
    for i in range(29, 30):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum