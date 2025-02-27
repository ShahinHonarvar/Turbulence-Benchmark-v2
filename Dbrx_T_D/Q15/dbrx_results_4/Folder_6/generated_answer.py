def sum_odd_ints_inclusive(input_list):
    if len(input_list) < 66:
        return 'Input list is too short. Should have at least 66 elements.'
    sum_of_odd_ints = 0
    for i in range(10, 67):
        if input_list[i] % 2 != 0:
            sum_of_odd_ints += input_list[i]
    return sum_of_odd_ints