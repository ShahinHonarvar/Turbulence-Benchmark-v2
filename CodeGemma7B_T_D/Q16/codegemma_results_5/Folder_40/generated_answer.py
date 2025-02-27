def sum_even_ints_inclusive(input_list):
    sum_evens = 0
    for i in range(0, 3, 1):
        if input_list[i] % 2 == 0:
            sum_evens += input_list[i]
    if sum_evens == 0:
        return 0
    else:
        return sum_evens