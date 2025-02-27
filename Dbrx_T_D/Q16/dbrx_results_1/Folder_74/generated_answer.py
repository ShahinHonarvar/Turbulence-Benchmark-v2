def sum_even_ints_inclusive(input_list):
    start_index = 17
    end_index = 78
    even_sum = 0
    for i in range(start_index, end_index + 1):
        if i < len(input_list) and input_list[i] % 2 == 0:
            even_sum += input_list[i]
    return even_sum