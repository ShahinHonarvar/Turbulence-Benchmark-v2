def all_even_ints_exclusive(input_list):
    result_list = []
    for i in range(44, 78):
        if input_list[i] % 2 == 0:
            result_list.append(input_list[i])
    return result_list