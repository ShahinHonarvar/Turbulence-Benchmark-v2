def sum_even_ints_inclusive(input_list):
    sum_value = int()
    for i in range(4, 5):
        if input_list[i] % 2 == 0:
            sum_value += input_list[i]
    return sum_value