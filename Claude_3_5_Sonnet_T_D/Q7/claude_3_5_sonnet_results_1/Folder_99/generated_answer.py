def all_even_ints_inclusive(integer_list):
    start_index = 310
    end_index = 371
    result = []
    for i in range(start_index, end_index):
        if i < len(integer_list) and integer_list[i] % 2 == 0:
            result.append(integer_list[i])
    return result