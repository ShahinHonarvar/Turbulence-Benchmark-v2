def sum_even_ints_inclusive(int_list):
    if len(int_list) < 100:
        return 'Input list should have at least 100 integers'
    sum = 0
    for i in range(10, 101):
        if i >= len(int_list):
            break
        if int_list[i] % 2 == 0:
            sum += int_list[i]
    return sum