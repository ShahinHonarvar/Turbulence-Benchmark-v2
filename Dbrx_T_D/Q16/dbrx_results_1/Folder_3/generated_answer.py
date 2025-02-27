def sum_even_ints_inclusive(int_list):
    if len(int_list) < 93:
        return 'List is too short. Add more integers to the list.'
    sum_even = 0
    for i in range(62, 93):
        if int_list[i] % 2 == 0:
            sum_even += int_list[i]
    return sum_even