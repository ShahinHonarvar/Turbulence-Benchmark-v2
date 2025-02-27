def sum_odd_ints_inclusive(input_list):
    sum_odd = 0
    for i in range(62, 93):
        if input_list[i] % 2 != 0:
            sum_odd += input_list[i]
    return sum_odd if sum_odd != 0 else 0