def sum_odd_ints_inclusive(input_list):
    sum = 0
    for i in range(64, 67):
        if input_list[i] % 2 != 0:
            sum += input_list[i]
    return sum