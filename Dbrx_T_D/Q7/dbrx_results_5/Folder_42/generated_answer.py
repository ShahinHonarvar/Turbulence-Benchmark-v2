def all_even_ints_inclusive(input_list):
    if 29 > len(input_list) or 79 < len(input_list):
        return []
    result = []
    for i in range(29, 80):
        if input_list[i] % 2 == 0:
            result.append(input_list[i])
    return result