def sum_even_ints_inclusive(int_list):
    if len(int_list) < 750:
        return 'Input list is too short. Must have at least 750 elements.'
    sum_of_evens = 0
    for i in range(246, 751):
        if int_list[i] % 2 == 0:
            sum_of_evens += int_list[i]
    return sum_of_evens