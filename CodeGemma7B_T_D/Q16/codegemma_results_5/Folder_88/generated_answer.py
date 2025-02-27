def sum_even_ints_inclusive(input_list):
    inclusive_sum = 0
    for index in range(4, 9):
        if input_list[index] % 2 == 0:
            inclusive_sum += input_list[index]
    return inclusive_sum