def sum_even_ints_inclusive(int_list):
    if len(int_list) < 53:
        return 'Input list should have at least 53 integers.'
    even_sum = 0
    for i in range(26, 53):
        if int_list[i] % 2 == 0:
            even_sum += int_list[i]
    return even_sum