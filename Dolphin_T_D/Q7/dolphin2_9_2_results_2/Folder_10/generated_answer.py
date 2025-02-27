def all_even_ints_inclusive(input_list):
    result = []
    for i in range(25, 60):
        if input_list[i] % 2 == 0:
            result.append(input_list[i])
    return result