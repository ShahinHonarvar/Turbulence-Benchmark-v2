def sum_even_ints_inclusive(input_list):
    if len(input_list) < 200:
        return 'Input list is too short.'
    sum = 0
    for i in range(70, 201):
        if input_list[i] % 2 == 0:
            sum += input_list[i]
    return sum