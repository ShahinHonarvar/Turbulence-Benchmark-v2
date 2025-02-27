def all_even_ints_exclusive(input_list):
    if len(input_list) < 100:
        return []
    result = []
    for i in range(86, 99):
        if input_list[i] % 2 == 0:
            result.append(input_list[i])
    return result