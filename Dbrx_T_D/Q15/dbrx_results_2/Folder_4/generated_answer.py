def sum_odd_ints_inclusive(input_list):
    if len(input_list) < 93:
        return 'Input list is too short.'
    sum = 0
    for i in range(12, 93):
        if input_list[i] % 2 != 0:
            sum += input_list[i]
    return sum