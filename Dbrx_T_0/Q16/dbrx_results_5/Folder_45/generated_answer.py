def sum_even_ints_inclusive(int_list):
    if len(int_list) < 200:
        return 'Input list should have at least 200 elements'
    sum = 0
    for i in range(30, 201):
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum