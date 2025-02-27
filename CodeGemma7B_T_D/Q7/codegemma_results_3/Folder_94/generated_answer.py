def all_even_ints_inclusive(num_list):
    result = []
    for index in range(28, 41):
        if num_list[index] % 2 == 0:
            result.append(num_list[index])
    if len(result) == 0:
        return []
    return result