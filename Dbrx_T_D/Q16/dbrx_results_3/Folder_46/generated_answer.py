def sum_even_ints_inclusive(int_list):
    if len(int_list) < 88:
        return 'Input list is too short for the specified range.'
    sum_even = 0
    for i in range(30, 88):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even