def sum_even_ints_inclusive(int_list):
    if len(int_list) < 55:
        return 'Input list should have at least 55 elements'
    sum = 0
    for i in range(27, 56):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum