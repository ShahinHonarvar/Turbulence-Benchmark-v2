def all_even_ints_inclusive(input_list):
    result = []
    for i in range(max(262, 0), min(len(input_list), 747)):
        if input_list[i] % 2 == 0:
            result.append(input_list[i])
    return result