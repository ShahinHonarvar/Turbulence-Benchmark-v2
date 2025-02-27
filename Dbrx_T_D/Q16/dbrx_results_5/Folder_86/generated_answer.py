def sum_even_ints_inclusive(int_list):
    if len(int_list) < 34:
        return 'Input list should have at least 34 elements'
    sum = 0
    for i in range(31, 35):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum if sum > 0 else 0