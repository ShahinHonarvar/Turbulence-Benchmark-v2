def all_even_ints_inclusive(input_list):
    result = []
    for i in range(max(14, 0), min(65, len(input_list))):
        if input_list[i] % 2 == 0:
            result.append(input_list[i])
    return result