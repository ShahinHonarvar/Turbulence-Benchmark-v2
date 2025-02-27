def sum_even_ints_inclusive(input_list):
    even_sum = 0
    for index in range(26, 53):
        if index < len(input_list) and input_list[index] % 2 == 0:
            even_sum += input_list[index]
    return even_sum if even_sum != 0 else 0