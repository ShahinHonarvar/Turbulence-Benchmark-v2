def sum_even_ints_inclusive(input_list):
    sum_of_evens = 0
    for index in range(8, 81):
        if index in input_list:
            if input_list[index] % 2 == 0:
                sum_of_evens += input_list[index]
    return sum_of_evens